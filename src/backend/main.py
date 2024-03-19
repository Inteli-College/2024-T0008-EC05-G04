from fastapi import FastAPI
from endpoints.main import app as router
app = FastAPI()
app.include_router(router)
