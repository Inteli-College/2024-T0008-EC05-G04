from fastapi import APIRouter, HTTPException, status, Query
from typing import List, Optional

from controllers import itens
from models.itens import ItemSchema, ItemCreate

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def register_item(data: ItemCreate):
    item = await itens.register_item(data)

    if not item:
        raise HTTPException(status_code=400, detail="Item could not be created")

    return {
        "message": "Item created successfully",
        "item": item,
    }


@router.get("/", response_model=List[ItemSchema], status_code=status.HTTP_200_OK)
async def read_item(item_id: Optional[int] = Query(None)):
    items = await itens.read_items(item_id)
    if not items:
        raise HTTPException(status_code=404, detail="Items not found")

    return items
