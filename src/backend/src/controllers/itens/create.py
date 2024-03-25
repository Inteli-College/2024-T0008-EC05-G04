from models.itens import ItemCreate
from dbconnect import (
    conn_postgres,
)


async def register_item(item: ItemCreate):
    async with conn_postgres.transaction():
        try:
            query = """
            INSERT INTO itens (name, expire, manufacturer, batch) 
            VALUES ($1, $2, $3, $4) RETURNING id;
            """
            # Execute a consulta passando os valores diretamente
            id_of_new_item = await conn_postgres.fetchval(query, item.name)
            # Retorna uma resposta de sucesso com o ID do novo item
            return {"detail": "Item added successfully", "id": id_of_new_item}
        except:
            return {"detail": "Error adding item"}
