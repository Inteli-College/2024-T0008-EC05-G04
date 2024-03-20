from fastapi import HTTPException, APIRouter, status
from schemas import KitOrderCreate, KitPositionSchema
from dbconnect import conn_postgres
from aiohttp import ClientSession
from asyncio import run
import json

app = APIRouter()


async def kit_position_find(kit_id: int):
    query = """
    SELECT id, kit_id, position, item_id FROM kit_positions WHERE kit_id = $1;
    """
    return await conn_postgres.fetch(query, kit_id)


async def post_data(url, data):
    async with ClientSession() as session:  # Cria uma sessão assíncrona
        async with session.post(url, json=data) as response:  # Faz a chamada POST
            response_data = await response.text()  # Aguarda a resposta
            return response_data


@app.post("/kit-order", status_code=status.HTTP_201_CREATED)
async def create_kit_order(kit_order: KitOrderCreate):
    async with conn_postgres.transaction():
        try:

            async def send_to_production():
                url = "http://10.150.4.91:5000/kit-order"
                rows = await kit_position_find(kit_order.kit_id)
                to_production = [KitPositionSchema(**row) for row in rows]
                print(to_production[0].id)
                kit_positions_json = json.dumps(
                    [kit_position.dict() for kit_position in to_production], indent=4
                )
                print(kit_positions_json)
                response = await post_data(url, kit_positions_json)
                return response

            robot_response = await run(send_to_production())

            if robot_response == "OK":
                query = """
                INSERT INTO kit_order (status, kit_id, date, requested_by)
                VALUES ($1, $2, NOW(), $3) RETURNING id;
                """

                id_of_new_kit_order = await conn_postgres.fetchval(
                    query, "pending", kit_order.kit_id, kit_order.requested_by
                )

                return {
                    "detail": "Kit order added successfully",
                    "id": id_of_new_kit_order,
                }
        except Exception as e:
            raise HTTPException(
                status_code=400, detail=f"Error adding kit order: {str(e)}"
            )
