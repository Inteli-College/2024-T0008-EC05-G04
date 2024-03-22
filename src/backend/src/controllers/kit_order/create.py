from typing import Optional
import requests

from dbconnect import conn_postgres
from models.kit_order import KitOrderCreate, KitOrderSchema
from get import get_kit_order_by_id
import tokens


async def send_kit_order_to_robot(kit_id: int):
    query = """
        SELECT id, kit_id, position, item_id FROM kit_positions WHERE kit_id = $1;
    """
    rows = await conn_postgres.fetch(query, kit_id)

    to_robot = [KitPositionSchema(**row) for row in rows]

    kit_positions = json.dumps(
        [kit_position.dict() for kit_position in to_robot], indent=4
    )

    response = requests.post(
        url=f"{tokens.ROBOT_URL}/kit-order",
        json=kit_positions,
    )

    return response


async def create_kit_order(kit_order: KitOrderCreate) -> Optional[KitOrderSchema]:
    async with conn_postgres.transaction():
        query = """
            INSERT INTO kit_order (status, kit_id, date, requested_by)
            VALUES ($1, $2, NOW(), $3) RETURNING id;
        """

        kit_order_id = await conn_postgres.fetchval(
            query, kit_order.status, kit_order.kit_id, kit_order.requested_by
        )

        robot_response = await send_kit_order_to_robot(kit_order_id)

        if robot_response.status_code == 200:
            return await get_kit_order_by_id(kit_order_id)

        return None
