from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import routers

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routers.router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
