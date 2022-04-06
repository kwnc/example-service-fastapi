from typing import Optional, List
from bson import ObjectId
from pydantic import BaseModel, Field

from app.models.py_object_id import PyObjectId
from app.models.order_model import OrderModel


class UserModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email: str
    password: str
    orders: Optional[List[OrderModel]] = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "email": "konrad@example.com",
                "password": "password"
            }
        }
