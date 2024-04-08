from typing import List, Optional
from models.kits import KitSchema

from dbconnect import conn_postgres


async def get_all() -> Optional[List[KitSchema]]:
    async with conn_postgres.transaction():
        query = """
        SELECT * FROM kits;
        """

        rows = await conn_postgres.fetch(query)

        if not rows:
            return None

        kits = [KitSchema(**row) for row in rows]

        return kits


async def get_by_id(kit_id: int) -> Optional[KitSchema]:
    query = "SELECT * FROM kits WHERE id = $1;"
    row = await conn_postgres.fetchrow(query, kit_id)

    if not row:
        return None

    return KitSchema(**row)
