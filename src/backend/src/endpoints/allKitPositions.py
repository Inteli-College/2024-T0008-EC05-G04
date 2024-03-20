from fastapi import HTTPException, APIRouter, status
from typing import List
from schemas import KitPositionSchema
from dbconnect import conn_postgres  # Certifique-se de que conn_postgres esteja configurado corretamente para asyncpg

app = APIRouter()

@app.get("/kit-positions/{kit_id}", response_model=List[KitPositionSchema], status_code=status.HTTP_200_OK)
async def get_kit_positions(kit_id: int):
    async with conn_postgres.transaction():
        query = """
        SELECT id, kit_id, position, item_id FROM kit_positions WHERE kit_id = $1;
        """
        rows = await conn_postgres.fetch(query, kit_id)
        if not rows:
            raise HTTPException(status_code=404, detail="Kit positions not found")
        # Convertendo os resultados da consulta para KitPositionSchema
        kit_positions = [KitPositionSchema(**row) for row in rows]
        return kit_positions
