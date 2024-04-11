from typing import List, Optional
from dbconnect import conn_postgres
from models.kit_orders import KitOrderSchema


async def get_all(requested_by: Optional[int] = None) -> Optional[List[dict]]:
    async with conn_postgres.transaction():
        if requested_by:
            query = """
                SELECT 
                    kit_order.id,
                    robots.name as robot_name, 
                    kits.name as kit_name, 
                    kit_order.status, 
                    kit_order.start_date, 
                    kit_order.end_date, 
                    kit_order.requested_by
                FROM 
                    kit_order
                JOIN 
                    robots ON kit_order.robot_id = robots.id
                JOIN 
                    kits ON kit_order.kit_id = kits.id
                WHERE 
                    kit_order.requested_by = $1;
            """
            rows = await conn_postgres.fetch(query, requested_by)
        else:
            query = """
                SELECT 
                    kit_order.id,
                    robots.name as robot_name, 
                    kits.name as kit_name, 
                    kit_order.status, 
                    kit_order.start_date, 
                    kit_order.end_date, 
                    kit_order.requested_by
                FROM 
                    kit_order
                JOIN 
                    robots ON kit_order.robot_id = robots.id
                JOIN 
                    kits ON kit_order.kit_id = kits.id;
            """
            rows = await conn_postgres.fetch(query)

        if not rows:
            return None

        # Construct a list of dictionaries directly from the rows
        orders = [
            {
                "id": row["id"],
                "robot_name": row["robot_name"],
                "kit_name": row["kit_name"],
                "status": row["status"],
                "start_date": row["start_date"],
                "end_date": row["end_date"],
                "requested_by": row["requested_by"],
            }
            for row in rows
        ]

        return orders


async def get_by_id(kit_order_id: int) -> Optional[KitOrderSchema]:
    async with conn_postgres.transaction():
        query = "SELECT * FROM kit_order WHERE id = $1;"
        row = await conn_postgres.fetchrow(query, kit_order_id)

        if not row:
            return None
        

        return KitOrderSchema(**row)
