from fastapi import APIRouter
from . import itens, kit_orders, kit_positions, kits, robots

router = APIRouter()

router.include_router(itens.router, prefix="/item")
router.include_router(kit_orders.router, prefix="/kit-order")
router.include_router(kit_positions.router, prefix="/kit-position")
router.include_router(kits.router, prefix="/kit")
router.include_router(robots.router, prefix="/robot")
