from fastapi import Query
from typing import Optional
from models.itens import ItemSchema
from dbconnect import (
    conn_postgres,
)


async def read_items(item_id: Optional[int] = Query(None)):
    async with conn_postgres.transaction():
        if item_id is not None:
            query = """
            SELECT id, name FROM itens WHERE id = $1;
            """
            rows = await conn_postgres.fetch(query, item_id)
        else:
            query = """
            SELECT id, name FROM itens;
            """
            rows = await conn_postgres.fetch(query)

        items = [ItemSchema(**row) for row in rows]
        return items
