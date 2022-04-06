from typing import Optional
from fastapi import APIRouter, Body, HTTPException, status, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.core.database import db
from app.models.order_model import OrderModel
from app.models.details import OrderStatus
from app.services import order_service

router = APIRouter(
    prefix='/api/v1/orders',
    tags=['order']
)


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
    if page == 1:
        orders = await db["order"].find({'order_status': order_status}).to_list(page_size)
    elif page == 2:
        orders = await db["order"].find({'order_status': order_status}).skip(page_size).to_list(page_size)
    else:
        orders = await db["order"].find({'order_status': order_status}).skip((page - 1) * page_size).to_list(
            page_size)
    response.status_code = status.HTTP_200_OK
    return {
        'orders': orders,
        'page': page,
        'page_size': page_size,
    }


@router.get("/{id}", response_model=OrderModel, status_code=status.HTTP_200_OK)
async def get_order(order_id: str):
    """
    Retrieves specific Order by ID

    - **id** mandatory path parameter
    """
    return order_service.get_by_id(order_id=order_id)


@router.delete("/{id}", response_description="Delete a order")
async def delete_order(order_id: str):
    delete_result = await db["order"].delete_one({"_id": order_id})
    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail=f"Order {order_id} not found")
