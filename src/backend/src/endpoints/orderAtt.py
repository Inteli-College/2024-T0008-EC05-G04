from fastapi import HTTPException, APIRouter, status as http_status
from dbconnect import conn_postgres
from schemas import KitOrderStatusUpdate

app = APIRouter()

@app.patch("/kit-order/{kit_order_id}/status", status_code=http_status.HTTP_200_OK)
async def update_kit_order_status(kit_order_id: int, kit_order_status_update: KitOrderStatusUpdate):
    async with conn_postgres.transaction():
        # Atualiza tanto o status quanto a data/hora para o momento atual
        query_order = """
        UPDATE kit_order SET status = $1, date = NOW() WHERE id = $2 RETURNING id;
        """
        updated_order_id = await conn_postgres.fetchval(query_order, kit_order_status_update.new_status, kit_order_id)
        
        if not updated_order_id:
            raise HTTPException(status_code=http_status.HTTP_404_NOT_FOUND, detail="KitOrder not found")

        # Aqui, assume-se que o incremento da quantidade é desejado como antes
        query_kits = """
        UPDATE kits SET quantity = quantity + 1 WHERE id = $1 RETURNING id;
        """
        updated_kit_id = await conn_postgres.fetchval(query_kits, kit_order_id)  # Supondo que kit_order_id é o kit_id

        if not updated_kit_id:
            raise HTTPException(status_code=http_status.HTTP_404_NOT_FOUND, detail="Kit not found based on KitOrder ID")

        return {
            "message": f"KitOrder with id {kit_order_id} status updated to '{kit_order_status_update.new_status}', date set to current timestamp, and Kit quantity incremented"
        }
