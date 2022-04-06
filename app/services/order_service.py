from fastapi import HTTPException, status

from app.core.database import db


async def get_by_id(order_id: str):
    if (order := await db["order"].find_one({"_id": order_id})) is not None:
        return order
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Order {order_id} not found")
