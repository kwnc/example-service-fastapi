from bson import ObjectId
from pydantic import BaseModel, Field
from app.models.py_object_id import PyObjectId


class VehicleModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    license_plate: str
    brand: str
    model: str
    
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        # schema_extra = {
        #     "example": {
        #         "vehicle": {
        #             "license_plate": "string",
        #             "brand": "string",
        #             "model": "string"
        #         },
        #         "services": "list of services",
        #         "images": [
        #             {
        #                 "url": "string",
        #                 "alias": "string"
        #             }
        #         ],
        #         "entry_date": "2022-04-06T16:21:19.914245",
        #         "exit_date": "2022-04-06T16:21:20.185Z",
        #         "order_status": "active",
        #         "observations": "string",
        #         "gasoline_level": "half",
        #         "drown": False,
        #         "driven": False,
        #         "scratched": False
        #     }
        # }
