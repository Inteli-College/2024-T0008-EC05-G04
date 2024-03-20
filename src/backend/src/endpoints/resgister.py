from fastapi import HTTPException, APIRouter
from schemas import UserCreate
from dbconnect import conn_postgres  # Ajuste para a função correta para obter a conexão asyncpg
from passlib.context import CryptContext

app = APIRouter()

# Cria uma instância do CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

@app.post("/register", status_code=201)
async def user_register(user: UserCreate):
    hashed_password = get_password_hash(user.password)
    async with conn_postgres.transaction():
        try:
            # Ajuste na consulta SQL para evitar o erro com a palavra reservada "user"
            query = "INSERT INTO users (\"user\", password) VALUES ($1, $2) RETURNING id;"
            user_id = await conn_postgres.fetchval(query, user.user, hashed_password)
            return {"detail": "User added successfully", "id": user_id}
        except Exception as e:
            # Este bloco catch capturará qualquer exceção, incluindo erros de SQL
            raise HTTPException(status_code=400, detail=f"Error adding user: {e}")
