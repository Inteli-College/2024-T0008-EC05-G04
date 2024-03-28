from pydantic import BaseModel


class KitSchema(BaseModel):
    id: int
    name: str


class KitCreate(BaseModel):
    name: str
