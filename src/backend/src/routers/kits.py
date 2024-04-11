from fastapi import APIRouter, HTTPException, status, Query
from typing import List, Optional

from controllers import kits
from models.kits import KitSchema, KitCreate

router = APIRouter()


@router.get("/")
async def get_all_kits():
    kits_list = await kits.get_all()

    if not kits_list:
        raise HTTPException(status_code=404, detail="No kits found")

    return kits_list


@router.get("/{kit_id}")
async def get_kit(kit_id: int):
    kit = await kits.get_by_id(kit_id)

    if not kit:
        raise HTTPException(status_code=404, detail="Kit not found")

    return kit


@router.post("/", status_code=status.HTTP_201_CREATED)
async def register_kit(data: KitCreate):
    kit = await kits.create(data)

    if not kit:
        raise HTTPException(status_code=400, detail="Kit could not be created")

    return {
        "message": "Kit created successfully",
        "kit": kit,
    }
