from fastapi import HTTPException, APIRouter
from schemas import KitCreate
from dbconnect import conn_postgres  # A função que retorna uma conexão asyncpg

app = APIRouter()

@app.post("/add-kit", status_code=201)
async def add_kit(kit: KitCreate):
    async with conn_postgres.transaction():
        try:
            # Preparando a query SQL para inserção, usando placeholders do asyncpg
            query = "INSERT INTO kits (name, quantity) VALUES ($1, $2)"
            # Execute a consulta passando os valores diretamente
            await conn_postgres.execute(query, kit.name, kit.quantity)
            # Retorna uma resposta de sucesso
            return {"detail": "Kit added successfully"}
        except Exception as e:
            # Levanta uma HTTPException para indicar falha
            raise HTTPException(status_code=400, detail=f"Error adding kit: {str(e)}")
