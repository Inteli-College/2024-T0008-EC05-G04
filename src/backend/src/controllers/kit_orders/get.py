from typing import List, Optional
from dbconnect import conn_postgres
from models.kit_orders import KitOrderSchema


async def get_all(requested_by: Optional[int] = None) -> Optional[List[KitOrderSchema]]:
    async with conn_postgres.transaction():
        if requested_by:
            query = "SELECT * FROM kit_order WHERE requested_by = $1;"
            rows = await conn_postgres.fetch(query, requested_by)
        else:
            query = "SELECT * FROM kit_order;"
            rows = await conn_postgres.fetch(query)

        if not rows:
            return None

        return [KitOrderSchema(**row) for row in rows]


async def get_by_id(kit_order_id: int) -> Optional[KitOrderSchema]:
    async with conn_postgres.transaction():
        query = "SELECT * FROM kit_order WHERE id = $1;"
        row = await conn_postgres.fetchrow(query, kit_order_id)

        if not row:
            return None

        print(row)

        return KitOrderSchema(**row)
