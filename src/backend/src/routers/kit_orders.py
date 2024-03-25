from fastapi import APIRouter, HTTPException, status
from typing import List

from controllers import kit_orders
from models.kit_orders import KitOrderSchema, KitOrderCreate

router = APIRouter()


@router.get("/", response_model=List[KitOrderSchema])
async def get_all_kit_orders():
    orders = await kit_orders.get_all()

    if not orders:
        raise HTTPException(status_code=404, detail="No kit orders found")

    return orders


@router.get("/{order_id}", response_model=KitOrderSchema)
async def get_kit_order(order_id: int):
    order = await kit_orders.get_by_id(order_id)

    if not order:
        raise HTTPException(status_code=404, detail="Kit order not found")

    return order


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_kit_order(data: KitOrderCreate):
    order = await kit_orders.create(data)

    if not order:
        raise HTTPException(status_code=400, detail="Kit order could not be created")

    return {
        "message": "Kit order created successfully",
        "kit_order": order,
    }
