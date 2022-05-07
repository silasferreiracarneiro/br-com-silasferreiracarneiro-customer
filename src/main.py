import uvicorn, logging, sys
from fastapi import FastAPI

from src.config import get_config
from src.db import db
from src.rest import customer

sys.setrecursionlimit(1500)

app = FastAPI(title="Async FastAPI")

app.include_router(customer.router, prefix='/api/customer')

@app.on_event("startup")
async def startup():
    config = get_config()
    await db.connect_to_database(path=config.db_path)


@app.on_event("shutdown")
async def shutdown():
    await db.close_database_connection()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)