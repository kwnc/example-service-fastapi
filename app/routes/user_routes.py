from fastapi import APIRouter, Body, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.core.database import db
from app.core.hash import Hash
from app.models.user_model import UserModel

router = APIRouter(
    prefix='/api/v1/users',
    tags=['user']
)


@router.post(path="", response_description="Add new user")
async def post_user(user: UserModel = Body(...)):
    user.password = Hash.bcrypt(user.password)
    user = jsonable_encoder(user)
    new_user = await db["user"].insert_one(user)
    created_user = await db["user"].find_one({"_id": new_user.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)
