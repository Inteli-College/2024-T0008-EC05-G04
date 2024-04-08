from dbconnect import conn_postgres


async def delete(robot_id: int) -> bool:
    async with conn_postgres.transaction():
        try:
            query = "DELETE FROM robots WHERE id = $1;"
            await conn_postgres.execute(query, robot_id)
            return True
        except Exception as e:
            print(f"Error deleting robot: {str(e)}")
            return False
