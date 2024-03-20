from datetime import date,datetime 
from pydantic import BaseModel

class KitSchema(BaseModel):
    id: int
    name: str
    quantity: int

class KitCreate(BaseModel):
    name: str
    quantity: int

class UserSchema(BaseModel):
    id: int
    user: str

class UserCreate(BaseModel):
    user: str
    password: str

class ItemSchema(BaseModel):
    id: int
    name: str
    expire: date
    manufacturer: str
    batch: str

class ItemCreate(BaseModel):
    name: str
    expire: date
    manufacturer: str
    batch: str

class KitPositionSchema(BaseModel):
    id: int
    kit_id: int
    position: int
    item_id: int

class KitPositionCreate(BaseModel):
    kit_id: int
    position: int
    item_id: int

class KitOrderSchema(BaseModel):
    id: int
    status: str  # Assumindo que 'status' será tratado como um campo de texto no backend
    kit_id: int
    date: datetime
    requested_by: int

class KitOrderCreate(BaseModel):
    kit_id: int
    requested_by: int


class KitOrderStatusUpdate(BaseModel):
    new_status: str
