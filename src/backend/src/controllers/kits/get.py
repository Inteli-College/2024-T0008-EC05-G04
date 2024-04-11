from typing import List, Optional
from models.kits import KitSchema
import json

from dbconnect import conn_postgres


async def get_all():
    async with conn_postgres.transaction():
        query = """
            SELECT
                jsonb_build_object(
                    'id', kits.id,
                    'name', kits.name,
                    'itens', jsonb_agg(
                        jsonb_build_object(
                            'item_id', itens.id,
                            'item_name', itens.name,
                            'item_position', kit_positions.position,
                            'quantity', kit_positions.quantity
                        )
                    )
                ) AS kit
            FROM
                kits
            JOIN
                kit_positions ON kits.id = kit_positions.kit_id
            JOIN
                itens ON kit_positions.item_id = itens.id
            GROUP BY
                kits.id;
        """

        rows = await conn_postgres.fetch(query)

        rows = [json.loads(row["kit"]) for row in rows]

        return rows

async def get_by_id(kit_id: int):
    query = """
        SELECT
            jsonb_build_object(
                'id', kits.id,
                'name', kits.name,
                'itens', jsonb_agg(
                    jsonb_build_object(
                        'item_id', itens.id,
                        'item_name', itens.name,
                        'item_position', kit_positions.position,
                        'quantity', kit_positions.quantity
                    )
                )
            ) AS kit
        FROM
            kits
        JOIN
            kit_positions ON kits.id = kit_positions.kit_id
        JOIN
            itens ON kit_positions.item_id = itens.id
        WHERE
            kits.id = $1
        GROUP BY
            kits.id;
    """

    row = await conn_postgres.fetchrow(query, kit_id)

    if not row:
        return None
    
    return json.loads(row["kit"])