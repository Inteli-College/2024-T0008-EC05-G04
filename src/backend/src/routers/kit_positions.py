from fastapi import HTTPException, APIRouter, status
from typing import List

from controllers import kit_positions
from models.kit_positions import KitPositionSchema, KitPositionCreate

router = APIRouter()


@router.get("/", response_model=List[KitPositionSchema])
async def get_all_kit_positions():
    kit_positions_list = await kit_positions.get_all()

    if not kit_positions_list:
        raise HTTPException(status_code=404, detail="No kit positions found")

    return kit_positions_list


@router.get("/{kit_id}", response_model=List[KitPositionSchema])
async def get_kit_positions(kit_id: int):
    kit_positions_list = await kit_positions.get_by_id(kit_id)

    if not kit_positions_list:
        raise HTTPException(status_code=404, detail="No kit positions found")

    return kit_positions_list


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_kit_position(data: KitPositionCreate):
    kit_position = await kit_positions.create(data)

    if not kit_position:
        raise HTTPException(status_code=400, detail="Kit position could not be created")

    return {
        "message": "Kit position created successfully",
        "kit_position": kit_position,
    }


@router.delete("/{item_id}", status_code=status.HTTP_200_OK)
async def delete_kit_position(item_id: int):
    deleted = await kit_positions.delete(item_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Kit position could not be deleted")

    return {"message": "Kit position deleted successfully", "item_id": item_id}
