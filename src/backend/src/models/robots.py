from pydantic import BaseModel 


class RobotSchema(BaseModel):
    id: int
    name: str
    route: str


class RobotCreate(BaseModel):
    name: str
    route: str
