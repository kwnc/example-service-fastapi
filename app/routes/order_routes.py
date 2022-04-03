from typing import Optional

from fastapi import APIRouter, status, Response

from app.models.order_model import OrderModel
from app.models.details import OrderStatus

router = APIRouter(
    prefix='/api/v1/orders',
    tags=['orders']
)

orders = []


@router.post(path="")
def post_order(new_order: OrderModel):
    orders.append(new_order)
    return {'data': new_order}


@router.get(path="", summary='Retrieve all orders with optional Order Status query parameter',
            description='Retrieves all orders with optional OrderStatus and non-optional Pagination query parameters',
            response_description='List of Orders with specific Order Status and pagination parameters')
def get_orders(response: Response, order_status: Optional[OrderStatus] = OrderStatus.active, page: int = 1,
               page_size: int = 10):
    response_orders = list(filter(lambda order: order.order_status == order_status, orders))
    if len(response_orders):
        response.status_code = status.HTTP_200_OK
        return {
            'orders': response_orders,
            'Page': page,
            'Page size': page_size
        }
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return 'No orders found'


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
