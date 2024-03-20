from fastapi import APIRouter
from controllers import kit_order

router = APIRouter()


@router.get("/")
async def get_all_kit_orders():
    return kit_order.get_all()


@router.post("/")
async def create_kit_order():
    return kit_order.create()
