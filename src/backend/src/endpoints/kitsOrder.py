from fastapi import HTTPException, APIRouter, Query
from typing import List, Optional
from schemas import KitOrderSchema
from dbconnect import conn_postgres

app = APIRouter()

@app.get("/kit-orders", response_model=List[KitOrderSchema])
async def get_kit_orders(requested_by: Optional[int] = Query(None)):
    if requested_by:
        query = "SELECT * FROM kit_order WHERE requested_by = $1;"
        rows = await conn_postgres.fetch(query, requested_by)
    else:
        query = "SELECT * FROM kit_order;"
        rows = await conn_postgres.fetch(query)

    if not rows:
        raise HTTPException(status_code=404, detail="No kit orders found")
    
    return [KitOrderSchema(**row) for row in rows]
