from fastapi import APIRouter, HTTPException, status
from typing import List

from controllers import kit_order
from models.kit_order import KitOrderSchema, KitOrderCreate

router = APIRouter()


@router.get("/", response_model=List[KitOrderSchema])
async def get_all_kit_orders():
    kit_orders = await kit_order.get_all()
    if not kit_orders:
        raise HTTPException(status_code=404, detail="No kit orders found")

    return kit_orders


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_kit_order(data: KitOrderCreate):
    order = await kit_order.create(data)

    if not order:
        raise HTTPException(status_code=400, detail="Kit order could not be created")

    return {
        "message": "Kit order created successfully",
        "kit_order": order,
    }
