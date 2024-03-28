from typing import Optional
from dbconnect import conn_postgres

from models.robots import RobotCreate, RobotSchema
from .get import get_by_id


async def create(robot: RobotCreate) -> Optional[RobotSchema]:
    async with conn_postgres.transaction():
        try:
            query = """
            INSERT INTO robots (name, route)
            VALUES ($1, $2)
            RETURNING id;
            """
            robot_id = await conn_postgres.fetchval(query, robot.name, robot.route)

            return await get_by_id(robot_id)

        except Exception as e:
            print(f"Error adding robot: {str(e)}")
            return None
