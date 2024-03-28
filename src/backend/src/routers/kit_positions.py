from fastapi import APIRouter, HTTPException, Path
from typing import List
from schemas.kit_positions import KitPositionSchema, KitPositionCreate
from controllers import kit_positions_controller as kit_positions

router = APIRouter()


@router.get("/", response_model=List[KitPositionSchema])
async def get_all_kit_positions():
    return await kit_positions.get_all()


@router.get("/{kit_position_id}", response_model=KitPositionSchema)
async def get_kit_position(
    kit_position_id: int = Path(..., title="The ID of the kit position to retrieve"),
):
    kit_position = await kit_positions.get(kit_position_id)
    if not kit_position:
        raise HTTPException(status_code=404, detail="Kit position not found")
    return kit_position


@router.post("/", response_model=KitPositionSchema, status_code=201)
async def create_kit_position(kit_position: KitPositionCreate):
    return await kit_positions.create(kit_position)
