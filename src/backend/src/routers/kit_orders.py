from fastapi import APIRouter, HTTPException, status
from typing import List

from controllers import kit_orders
from models.kit_orders import KitOrderSchema, KitOrderCreate, KitOrderUpdate

router = APIRouter()


@router.get("/")
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


@router.put("/{order_id}", status_code=status.HTTP_200_OK)
async def update_kit_order(order_id: int, data: KitOrderUpdate):
    updated = await kit_orders.update(order_id, data)

    if not updated:
        raise HTTPException(status_code=404, detail="Kit order not found")

    return {
        "message": "Kit order updated successfully",
        "order_id": order_id,
    }


@router.delete("/{order_id}", status_code=status.HTTP_200_OK)
async def delete_kit_order(order_id: int):
    deleted = await kit_orders.delete(order_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Kit order not found")

    return {
        "message": "Kit order deleted successfully",
        "order_id": order_id,
    }
