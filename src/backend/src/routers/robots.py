from fastapi import APIRouter, HTTPException, Path

from typing import List

from models.robots import RobotSchema, RobotCreate
from controllers import robots

router = APIRouter()


@router.get("/", response_model=List[RobotSchema])
async def get_all_robots():
    robots_list = await robots.get_all()

    if not robots_list:
        raise HTTPException(status_code=404, detail="No robots found")

    return robots_list


@router.get("/{robot_id}", response_model=RobotSchema)
async def get_robot(
    robot_id: int = Path(..., title="The ID of the robot to retrieve"),
):
    robot = await robots.get_by_id(robot_id)

    if not robot:
        raise HTTPException(status_code=404, detail="Robot not found")

    return robot


@router.post("/", response_model=RobotSchema, status_code=201)
async def create_robot(robot: RobotCreate):
    robot = await robots.create(robot)

    if not robot:
        raise HTTPException(status_code=400, detail="Error creating robot")

    return {"message": "Robot created successfully", "robot": robot}


@router.delete("/{robot_id}", response_model=RobotSchema)
async def delete_robot(
    robot_id: int = Path(..., title="The ID of the robot to delete"),
):
    robot = await robots.delete(robot_id)

    if not robot:
        raise HTTPException(status_code=404, detail="Robot not found")

    return {"message": "Robot deleted successfully", "robot": robot}
