from fastapi import HTTPException, APIRouter, Query
from typing import List, Optional
from schemas import KitOrderSchema
from dbconnect import conn_postgres

app = APIRouter()

@app.get("/execute", response_model=List[KitOrderSchema])
async def get_kit_orders_by_status(status: Optional[str] = Query(None)):
    if status:
        query = "SELECT * FROM kit_order WHERE status = $1;"
        rows = await conn_postgres.fetch(query, status)
    else:
        query = "SELECT * FROM kit_order;"
        rows = await conn_postgres.fetch(query)

    if not rows:
        raise HTTPException(status_code=404, detail="No kit orders found with the specified status")
    
    return [KitOrderSchema(**row) for row in rows]
