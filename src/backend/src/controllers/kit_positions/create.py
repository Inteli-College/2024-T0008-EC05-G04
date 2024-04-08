from models.kit_positions import KitPositionCreate
from dbconnect import conn_postgres

from .get import get_by_id


async def create(kit_position: KitPositionCreate):
    async with conn_postgres.transaction():
        try:
            query = """
            INSERT INTO kit_positions (kit_id, position, item_id, quantity)
            VALUES ($1, $2, $3, $4) RETURNING id;
            """
            kit_position_id = await conn_postgres.fetchval(
                query, kit_position.kit_id, kit_position.position, kit_position.item_id, kit_position.quantity
            )

            return await get_by_id(kit_position_id)
        except Exception:
            return None
