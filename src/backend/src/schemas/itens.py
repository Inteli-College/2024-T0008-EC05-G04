from pydantic import BaseModel


class ItemSchema(BaseModel):
    id: int
    name: str


class ItemCreate(BaseModel):
    name: str
