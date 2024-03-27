from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class KitOrderSchema(BaseModel):
    id: int
    robot_id: int
    status: str
    kit_id: int
    start_date: datetime
    end_date: Optional[datetime]
    requested_by: int


class KitOrderCreate(BaseModel):
    robot_id: int
    kit_id: int
    requested_by: int


class KitOrderStatusUpdate(BaseModel):
    new_status: str


class KitOrderUpdate(BaseModel):
    robot_id: Optional[int]
    kit_id: Optional[int]
    requested_by: Optional[int]
    status: Optional[str]
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    requested_by: Optional[int]


class KitOrderDelete(BaseModel):
    id: int
