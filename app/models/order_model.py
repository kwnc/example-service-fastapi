import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from bson import ObjectId

from app.models.details import OrderStatus, GasolineLevel
from app.models.vehicle_model import VehicleModel
from app.models.py_object_id import PyObjectId


class Image(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    url: str
    alias: str


class OrderModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    vehicle: VehicleModel
    services: Optional[str] = 'list of services'
    images: Optional[List[Image]] = None
    entry_date: datetime.datetime = datetime.datetime.now()
    exit_date: Optional[datetime.datetime] = None
    order_status: OrderStatus = OrderStatus.active
    observations: str
    gasoline_level: GasolineLevel = GasolineLevel.half
    drown: bool = False
    driven: bool = False
    scratched: bool = False

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        # schema_extra = {
        #     "example": {
        #         "name": "Jane Doe",
        #         "email": "jdoe@example.com",
        #         "course": "Experiments, Science, and Fashion in Nanophotonics",
        #         "gpa": "3.0",
        #     }
        # }


class UpdateOrderModel(BaseModel):
    vehicle: Optional[VehicleModel]
    services: Optional[str]
    images: Optional[List[Image]]
    exit_date: Optional[datetime.datetime]
    order_status: Optional[OrderStatus]
    observations: Optional[str]
    drown: Optional[bool]
    driven: Optional[bool]
    scratched: Optional[bool]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        # schema_extra = {
        #     "example": {
        #         "name": "Jane Doe",
        #         "email": "jdoe@example.com",
        #         "course": "Experiments, Science, and Fashion in Nanophotonics",
        #         "gpa": "3.0",
        #     }
        # }
