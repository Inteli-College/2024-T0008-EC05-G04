from pydantic import BaseModel


class KitPositionCreate(BaseModel):
    kit_id: int
    position: int
    item_id: int


class KitPositionSchema(BaseModel):
    id: int
    kit_id: int
    position: int
    item_id: int
