import datetime
from typing import Optional, List

from pydantic import BaseModel

from app.models.details import OrderStatus, GasolineLevel
from app.models.vehicle_model import VehicleModel


class Image(BaseModel):
    url: str
    alias: str


class OrderModel(BaseModel):
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
