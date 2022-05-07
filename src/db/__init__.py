from src.db.mongo_data_base import DatabaseManager
from src.db.impl.mongo_manager import MongoManager

db = MongoManager()

async def get_database() -> DatabaseManager:
    return db