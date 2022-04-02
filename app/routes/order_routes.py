from typing import Optional

from fastapi import APIRouter, status, Response

from app.models.order_status import OrderStatus

router = APIRouter(
    prefix='/api/v1/orders',
    tags=['orders']
)


@router.get(path="", summary='Retrieve all orders with optional Order Status query parameter',
            description='Retrieves all orders with optional OrderStatus and non-optional Pagination query parameters',
            response_description='List of Orders with specific Order Status and pagination parameters')
def get_orders(response: Response, order_status: Optional[OrderStatus] = OrderStatus.active, page: int = 1,
               page_size: int = 10):
    response.status_code = status.HTTP_200_OK
    return {'Orders with status:': order_status, 'Page': page, 'Page size': page_size}


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_order(response: Response, order_id: int, query: Optional[str] = None):
    """
    Retrieves specific Order by ID

    - **id** mandatory path parameter
    """
    if order_id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Order {order_id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {"Order with id": order_id, "query": query}


@router.post(path="")
def post_order():
    pass
