from typing import List, Optional
from models.kit_positions import KitPositionSchema
from dbconnect import conn_postgres


async def get_all() -> Optional[List[KitPositionSchema]]:
    async with conn_postgres.transaction():
        query = """
        SELECT * FROM kit_positions;
        """

        rows = await conn_postgres.fetch(query)

        if not rows:
            return None

        kit_positions = [KitPositionSchema(**row) for row in rows]

        return kit_positions


async def get_by_id(kit_id: int) -> Optional[List[KitPositionSchema]]:
    async with conn_postgres.transaction():
        query = """
        SELECT * FROM kit_positions WHERE id = $1;
        """
        rows = await conn_postgres.fetch(query, kit_id)

        if not rows:
            return None

        kit_positions = [KitPositionSchema(**row) for row in rows]
        return kit_positions
