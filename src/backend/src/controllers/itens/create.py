from models.itens import ItemCreate
from dbconnect import conn_postgres

from .get import get_by_id


async def create(item: ItemCreate):
    async with conn_postgres.transaction():
        try:
            query = """
            INSERT INTO itens (name)
            VALUES ($1)
            RETURNING id;
            """
            item_id = await conn_postgres.fetchval(query, item.name)

            return await get_by_id(item_id)

        except Exception as e:
            print(f"Error adding item: {str(e)}")
            return None
