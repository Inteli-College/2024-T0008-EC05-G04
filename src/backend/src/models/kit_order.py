from datetime import date, datetime
from pydantic import BaseModel

"""
Table kit_order{
  id serial [pk]
  robot_id integer
  status enum
  kit_id integer
  start_date timestamp
  end_date timestamp
  requested_by integer
}
"""


class KitOrderSchema(BaseModel):
    id: int
    robot_id: int
    status: str
    kit_id: int
    start_date: datetime
    end_date: datetime
    requested_by: int


class KitOrderCreate(BaseModel):
    robot_id: int
    kit_id: int
    requested_by: int


class KitOrderStatusUpdate(BaseModel):
    new_status: str


class KitOrderUpdate(BaseModel):
    robot_id: int
    kit_id: int
    requested_by: int
    status: str
    start_date: datetime
    end_date: datetime
    requested_by: int


class KitOrderDelete(BaseModel):
    id: int
