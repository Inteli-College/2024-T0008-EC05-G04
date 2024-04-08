from dbconnect import conn_postgres


async def delete(item_id: int):
    async with conn_postgres.transaction():
        try:
            query = "DELETE FROM kits WHERE id = $1;"
            await conn_postgres.execute(query, item_id)

            return True
        except Exception as e:
            print(f"Error deleting kit order: {str(e)}")
            return False
