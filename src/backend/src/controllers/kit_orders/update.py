from dbconnect import conn_postgres
from models.kit_orders import KitOrderUpdate


async def update(kit_order: KitOrderUpdate):
    async with conn_postgres.transaction():
        try:
            query = """
            UPDATE kit_order
            SET status = $1
            WHERE id = $2
            RETURNING id;
            """
            kit_order_id = await conn_postgres.fetchval(
                query, kit_order.status, kit_order.id
            )

            return kit_order_id

        except Exception as e:
            print(f"Error updating kit order: {str(e)}")
            return None
