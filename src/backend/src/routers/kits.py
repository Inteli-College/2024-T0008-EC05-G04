from fastapi import APIRouter, HTTPException, Path
from typing import List
from schemas.kits import KitSchema, KitCreate
from controllers import kits_controller as kits 

router = APIRouter()


@router.get("/", response_model=List[KitSchema])
async def get_all_kits():
    return await kits.get_all()


@router.get("/{kit_id}", response_model=KitSchema)
async def get_kit(kit_id: int = Path(..., title="The ID of the kit to retrieve")):
    kit = await kits.get(kit_id)
    if not kit:
        raise HTTPException(status_code=404, detail="Kit not found")
    return kit


@router.post("/", response_model=KitSchema, status_code=201)
async def create_kit(kit: KitCreate):
    return await kits.create(kit)
