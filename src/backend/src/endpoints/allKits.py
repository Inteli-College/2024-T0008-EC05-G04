from fastapi import APIRouter, HTTPException
from schemas import KitSchema 
from typing import List
from dbconnect import conn_postgres
app = APIRouter()

@app.get("/kits", response_model=List[KitSchema])
async def read_kits_with_id_one():
    async with conn_postgres.transaction():
        rows = await conn_postgres.fetch("SELECT * FROM kits;")
        if not rows:
            raise HTTPException(status_code=404, detail="Kits not found")
        return [KitSchema(**row) for row in rows]