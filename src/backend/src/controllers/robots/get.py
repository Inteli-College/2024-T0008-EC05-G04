from typing import List, Optional
from models.robots import RobotSchema, RobotCreate

from dbconnect import conn_postgres


async def get_all() -> Optional[List[RobotSchema]]:
    async with conn_postgres.transaction():
        query = """
        SELECT * FROM robots;
        """

        rows = await conn_postgres.fetch(query)

        if not rows:
            return None

        robots = [RobotSchema(**row) for row in rows]

        return robots


async def get_by_id(robot_id: int) -> Optional[RobotSchema]:
    query = "SELECT * FROM robots WHERE id = $1;"
    row = await conn_postgres.fetchrow(query, robot_id)

    if not row:
        return None

    return RobotSchema(**row)
