from pydantic import BaseModel, Optional


class RobotSchema(BaseModel):
    id: int
    name: str
    route: str


class RobotCreate(BaseModel):
    name: str
    route: str
