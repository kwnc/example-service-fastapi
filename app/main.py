from fastapi import FastAPI, Depends, status, Response
from fastapi.openapi.utils import get_openapi

from app.config import get_settings, Settings
from app.routes import order_routes

app = FastAPI()
app.include_router(order_routes.router)


@app.get("/")
def read_root():
    return {"Welcome to Autolify Web Service API"}


@app.get("/ping", tags=['configuration'])
async def pong(response: Response, settings: Settings = Depends(get_settings)):
    response.status_code = status.HTTP_200_OK
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }


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
