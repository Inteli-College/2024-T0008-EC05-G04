from fastapi import HTTPException, APIRouter, status, Query
from typing import List, Optional
from schemas import ItemSchema
from dbconnect import conn_postgres  # Certifique-se de que conn_postgres esteja corretamente configurado para asyncpg

app = APIRouter()

@app.get("/itens", response_model=List[ItemSchema], status_code=status.HTTP_200_OK)
async def read_items(item_id: Optional[int] = Query(None)):
    async with conn_postgres.transaction():
        if item_id is not None:
            query = """
            SELECT id, name, expire, manufacturer, batch FROM itens WHERE id = $1;
            """
            rows = await conn_postgres.fetch(query, item_id)
        else:
            query = """
            SELECT id, name, expire, manufacturer, batch FROM itens;
            """
            rows = await conn_postgres.fetch(query)

        if not rows:
            raise HTTPException(status_code=404, detail="Items not found")
        
        items = [ItemSchema(**row) for row in rows]
        return items
