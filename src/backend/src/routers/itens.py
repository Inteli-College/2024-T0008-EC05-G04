from fastapi import APIRouter, HTTPException, status, Query
from typing import List, Optional

from controllers import itens
from models.itens import ItemSchema, ItemCreate

router = APIRouter()


@router.get("/", response_model=List[ItemSchema])
async def get_all_itens():
    itens_list = await itens.get_all()

    if not itens_list:
        raise HTTPException(status_code=404, detail="No itens found")

    return itens_list


@router.get("/{item_id}", response_model=List[ItemSchema])
async def get_item(item_id: int):
    item = await itens.get_by_id(item_id)

    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    return item


@router.post("/", status_code=status.HTTP_201_CREATED)
async def register_item(data: ItemCreate):
    item = await itens.create(data)

    if not item:
        raise HTTPException(status_code=400, detail="Item could not be created")

    return {
        "message": "Item created successfully",
        "item": item,
    }


@router.delete("/{item_id}", status_code=status.HTTP_200_OK)
async def delete_item(item_id: int):
    deleted = await itens.delete(item_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")

    return {
        "message": "Item deleted successfully",
        "item_id": item_id,
    }
