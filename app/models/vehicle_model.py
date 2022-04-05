from pydantic import BaseModel, Field
from app.models.py_object_id import PyObjectId


class VehicleModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    license_plate: str
    brand: str
    model: str
