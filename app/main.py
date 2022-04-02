from typing import Optional

from fastapi import FastAPI, Depends, status, Response
from fastapi.openapi.utils import get_openapi

from app.config import get_settings, Settings

from app.models.order_status import OrderStatus

app = FastAPI()


@app.get("/")
def read_root():
    return {"Welcome to Autolify Web Service API"}


@app.get("/api/v1/ping")
async def pong(response: Response, settings: Settings = Depends(get_settings)):
    response.status_code = status.HTTP_200_OK
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }


@app.get("/api/v1/orders")
def get_orders(response: Response, order_status: Optional[OrderStatus] = OrderStatus.active, page: int = 1,
               page_size: int = 10):
    response.status_code = status.HTTP_200_OK
    return {'Orders with status:': order_status, 'Page': page, 'Page size': page_size}


@app.get("/api/v1/orders/{id}", status_code=status.HTTP_200_OK)
def get_order(response: Response, order_id: int, query: Optional[str] = None):
    if order_id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Order {order_id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {"Order with id": order_id, "query": query}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Autolify Web Service FastAPI",
        version="0.1.3",
        description="This is Autolify API Schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://res.cloudinary.com/naprawumisia-pl/image/upload/v1648750647/autolify-logo.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
