from typing import Optional

from fastapi import FastAPI, Depends
from fastapi.openapi.utils import get_openapi

from app.config import get_settings, Settings

from app.models.order_status import OrderStatus

app = FastAPI()


@app.get("/")
def read_root():
    return {"Welcome to Autolify Web Service API"}


@app.get("/api/v1/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }


@app.get("/api/v1/orders")
def get_orders(status: Optional[OrderStatus] = OrderStatus.active):
    return {'message': f'All orders provided with status: {status}'}


@app.get("/api/v1/orders/{id}")
def get_order(order_id: int, query: Optional[str] = None):
    return {"Order with id": order_id, "query": query}


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Autolify Web Service FastAPI",
        version="0.1.1",
        description="This is Autolify API Schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://res.cloudinary.com/naprawumisia-pl/image/upload/v1648750647/autolify-logo.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
