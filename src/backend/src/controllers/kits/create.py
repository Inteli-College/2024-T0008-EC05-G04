from typing import Optional
from dbconnect import conn_postgres

from models.kits import KitCreate
from .get import get_by_id 
from schemas import KitSchema


async def create(kit: KitCreate) -> Optional[KitSchema]:
    async with conn_postgres.transaction():
        try:
            query = """
            INSERT INTO kits (name, quantity)
            VALUES ($1, $2)
            RETURNING id;
            """
            kit_id = await conn_postgres.execute(query, kit.name, kit.quantity)

            return await get_by_id(kit_id)

        except Exception as e:
            print(f"Error adding kit: {str(e)}")
            return None
