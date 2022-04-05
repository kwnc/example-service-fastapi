from typing import Optional
from fastapi import APIRouter, Body, HTTPException, status, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.models.order_model import OrderModel
from app.models.details import OrderStatus
from app.core.database import db

router = APIRouter(
    prefix='/api/v1/orders',
    tags=['orders']
)


def required_functionality():
    return {'message': 'Learning FastAPI is important'}


@router.post(path="", response_description="Add new order")
async def post_order(order: OrderModel = Body(...)):
    order = jsonable_encoder(order)
    new_order = await db["order"].insert_one(order)
    created_order = await db["order"].find_one({"_id": new_order.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_order)


@router.get(path="", summary='Retrieve all orders with optional Order Status query parameter',
            description='Retrieves all orders with optional OrderStatus and non-optional Pagination query parameters',
            response_description='List of Orders with specific Order Status and pagination parameters')
async def get_orders(response: Response, order_status: Optional[OrderStatus] = OrderStatus.active, page: int = 1,
                     page_size: int = 10):
    orders = await db["order"].find({'order_status': order_status}).to_list(page_size)
    if len(orders):
        response.status_code = status.HTTP_200_OK
        return {
            'orders': orders,
            'page': page,
            'page_size': page_size,
        }
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'No orders found with status': order_status}


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_order(order_id: str, query: Optional[str] = None):
    """
    Retrieves specific Order by ID

    - **id** mandatory path parameter
    """
    if (order := await db["order"].find_one({"_id": order_id})) is not None:
        return {
            'order': order,
            'query': query
        }
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student {order_id} not found")
