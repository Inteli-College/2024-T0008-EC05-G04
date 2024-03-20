from fastapi import FastAPI
import uvicorn

import routers

app = FastAPI()

app.include_router(routers.router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
