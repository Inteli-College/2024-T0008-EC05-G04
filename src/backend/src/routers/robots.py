from fastapi import APIRouter, HTTPException, Path
from typing import List
from schemas.robots import RobotSchema, RobotCreate
from controllers import robots_controller as robots

router = APIRouter()


@router.get("/", response_model=List[RobotSchema])
async def get_all_kits():
    return await robots.get_all()


@router.get("/{kit_id}", response_model=RobotSchema)
async def get_kit(kit_id: int = Path(..., title="The ID of the robot to retrieve")):
    robot = await robots.get(kit_id)
    if not robot:
        raise HTTPException(status_code=404, detail="Robot not found")
    return robot


@router.post("/", response_model=RobotSchema, status_code=201)
async def create_kit(robot: RobotCreate):
    return await robots.create(robot)
