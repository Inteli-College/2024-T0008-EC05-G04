from typing import Optional
import requests
import json
from dbconnect import conn_postgres
from models.kit_orders import KitOrderCreate, KitOrderSchema
from models.kit_positions import KitPositionSchema
from .get import get_by_id
from controllers import kits
import tokens


async def send_kit_order_to_robot(kit_id: int, kit_order: int):
    kit = await kits.get_by_id(kit_id)

    body = {"kit_order_id": kit_order, "kit": kit}

    url = tokens.ROBOT_URL + '/kit-order'

    response = requests.post(
        url=url,
        json=body,
    )

    return response


async def create(kit_order: KitOrderCreate) -> Optional[KitOrderSchema]:
    async with conn_postgres.transaction():
        initital_status = "requested"
        query = """
            INSERT INTO kit_order (status, kit_id, start_date, requested_by, robot_id)
            VALUES ($1, $2, NOW(), $3, $4) RETURNING id;
        """

        kit_order_id = await conn_postgres.fetchval(
            query,
            initital_status,
            kit_order.kit_id,
            kit_order.requested_by,
            kit_order.robot_id,
        )

        query = """
                UPDATE kit_order
                SET status = 'processing'
                WHERE id = $1;
            """
        await conn_postgres.execute(query, kit_order_id)

        robot_response = await send_kit_order_to_robot(kit_order.kit_id, kit_order_id)

        if robot_response.status_code == 200:
            returned_kit_order = await get_by_id(kit_order_id)

            query = """
                UPDATE kit_order
                SET status = 'completed'
                WHERE id = $1;
            """
            await conn_postgres.execute(query, kit_order_id)

            query = """
                UPDATE kit_order
                SET end_date = NOW()
                WHERE id = $1;
            """
            await conn_postgres.execute(query, kit_order_id)


            return returned_kit_order
        

        return None