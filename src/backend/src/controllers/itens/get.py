from typing import List, Optional
from models.itens import ItemSchema
from dbconnect import conn_postgres


async def get_all() -> Optional[List[ItemSchema]]:
    async with conn_postgres.transaction():
        query = """
        SELECT * FROM itens;
        """

        rows = await conn_postgres.fetch(query)

        if not rows:
            return None

        items = [ItemSchema(**row) for row in rows]

        return items


async def get_by_id(item_id: int) -> Optional[List[ItemSchema]]:
    async with conn_postgres.transaction():
        query = "SELECT * FROM itens WHERE id = $1;"
        rows = await conn_postgres.fetch(query, item_id)

        if not rows:
            return None

        items = [ItemSchema(**row) for row in rows]
        return items
