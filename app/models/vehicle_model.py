from pydantic import BaseModel


class VehicleModel(BaseModel):
    license_plate: str
    brand: str
    model: str
