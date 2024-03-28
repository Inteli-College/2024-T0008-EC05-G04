from fastapi import APIRouter, HTTPException, Path
from typing import List
from schemas.kit_orders import KitOrderSchema, KitOrderCreate
from controllers import kit_orders_controller as kit_orders

router = APIRouter()


@router.get("/", response_model=List[KitOrderSchema])
async def get_all_kit_orders():
    return await kit_orders.get_all()


@router.get("/{kit_order_id}", response_model=KitOrderSchema)
async def get_kit_order(
    kit_order_id: int = Path(..., title="The ID of the kit order to retrieve"),
):
    kit_order = await kit_orders.get(kit_order_id)
    if not kit_order:
        raise HTTPException(status_code=404, detail="Kit order not found")
    return kit_order


@router.post("/", response_model=KitOrderSchema, status_code=201)
async def create_kit_order(kit_order: KitOrderCreate):
    return await kit_orders.create(kit_order)
