from fastapi import HTTPException, APIRouter, status
from schemas import KitPositionCreate
from dbconnect import conn_postgres  # Supõe que conn_postgres é sua conexão asyncpg configurada

app = APIRouter()

@app.post("/kitPositionCreate", status_code=status.HTTP_201_CREATED)
async def kit_position_create(kit_position: KitPositionCreate):
    async with conn_postgres.transaction():
        try:
            query = """
            INSERT INTO kit_positions (kit_id, position, item_id) 
            VALUES ($1, $2, $3) RETURNING id;
            """
            # Execute a consulta passando os valores diretamente
            id_of_new_kit_position = await conn_postgres.fetchval(query, kit_position.kit_id, kit_position.position, kit_position.item_id)
            # Retorna uma resposta de sucesso com o ID da nova posição do kit
            return {"detail": "Kit position added successfully", "id": id_of_new_kit_position}
        except Exception as e:
            # Uma exceção lançada dentro de um bloco de transação faz com que a transação seja revertida automaticamente
            raise HTTPException(status_code=400, detail=f"Error adding kit position: {str(e)}")
