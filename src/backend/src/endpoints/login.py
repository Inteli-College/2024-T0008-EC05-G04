from fastapi import HTTPException, APIRouter, status
from schemas import UserCreate
from dbconnect import conn_postgres  # A função que retorna uma conexão asyncpg
from passlib.context import CryptContext

app = APIRouter()

# contexto do Passlib para hashing de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

async def authenticate_user(username: str, password: str):
    query = "SELECT * FROM users WHERE user = $1;"
    user = await conn_postgres.fetchrow(query, username)
    if not user:
        return False
    # Como 'user' é um Record, você acessa colunas como atributos ou por índice
    if not await verify_password(password, user['password']):
        return False
    return user  # Retorna o usuário como um dict

@app.post("/login", status_code=status.HTTP_200_OK)
async def login(user_credentials: UserCreate):
    user = await authenticate_user(user_credentials.user, user_credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"message": "Login successful!"}
