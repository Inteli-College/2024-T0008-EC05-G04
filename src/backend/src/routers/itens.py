from fastapi import APIRouter, HTTPException, Path
from typing import List
from schemas.itens import ItemSchema, ItemCreate
from controllers import itens_controller as itens

router = APIRouter()


@router.get("/", response_model=List[ItemSchema])
async def get_all_items():
    return await itens.get_all()


@router.get("/{item_id}", response_model=ItemSchema)
async def get_item(item_id: int = Path(..., title="The ID of the item to retrieve")):
    item = await itens.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/", response_model=ItemSchema, status_code=201)
async def create_item(item: ItemCreate):
    return await itens.create(item)
