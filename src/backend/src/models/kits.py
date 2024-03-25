from pydantic import BaseModel


class KitSchema(BaseModel):
    id: int
    name: str
    quantity: int


class KitCreate(BaseModel):
    name: str
    quantity: int
