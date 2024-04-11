from typing import Optional
from dbconnect import conn_postgres

from models.kits import KitCreate
from .get import get_by_id
from models.kits import KitSchema


async def create(kit: KitCreate) -> Optional[KitSchema]:
    async with conn_postgres.transaction():
        try:
            query = """
            INSERT INTO kits (name)
            VALUES ($1)
            RETURNING id;
            """
            kit_id = await conn_postgres.fetchval(query, kit.name)

            # retorna um json com {kit_id: kit_id}
            return {
                "id": kit_id,
                "name": kit.name
            }

        except Exception as e:
            print(f"Error adding kit: {str(e)}")
            return None
