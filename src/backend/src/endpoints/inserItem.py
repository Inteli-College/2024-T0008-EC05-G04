from fastapi import HTTPException, APIRouter, status
from schemas import ItemCreate
from dbconnect import conn_postgres  # Certifique-se de que conn_postgres retorne uma conexão asyncpg configurada

app = APIRouter()

@app.post("/item-register", status_code=status.HTTP_201_CREATED)
async def register_item(item: ItemCreate):
    async with conn_postgres.transaction():
        try:
            query = """
            INSERT INTO itens (name, expire, manufacturer, batch) 
            VALUES ($1, $2, $3, $4) RETURNING id;
            """
            # Execute a consulta passando os valores diretamente
            id_of_new_item = await conn_postgres.fetchval(query, item.name, item.expire, item.manufacturer, item.batch)
            # Retorna uma resposta de sucesso com o ID do novo item
            return {"detail": "Item added successfully", "id": id_of_new_item}
        except Exception as e:
            # Uma exceção lançada dentro de um bloco de transação faz com que a transação seja revertida automaticamente
            raise HTTPException(status_code=400, detail=f"Error adding item: {str(e)}")
