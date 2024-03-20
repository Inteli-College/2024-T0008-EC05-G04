from fastapi import APIRouter
from . import kit_order

router = APIRouter()

router.include_router(kit_order.router, prefix="/kit-order")
