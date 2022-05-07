import logging
import asyncio

from typing import List

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from src.db.mongo_data_base import DatabaseManager
from src.db.models import CustomerDB, OID


class MongoManager(DatabaseManager):
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

    async def connect_to_database(self, path: str):
        logging.info("Connecting to MongoDB.")

        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        self.client = AsyncIOMotorClient(
            path,
            io_loop=loop,
            maxPoolSize=10,
            minPoolSize=10)

        self.db = self.client["customer_db"]

        print(self.db, flush=True)

        logging.info("Connected to MongoDB.")

    async def close_database_connection(self):
        logging.info("Closing connection with MongoDB.")
        self.client.close()
        logging.info("Closed connection with MongoDB.")

    async def get_customers(self) -> List[CustomerDB]:
        customer_list = []
        customers = self.db.customer_tb.find()
        print(customers, flush=True)

        async for customer in customers:
            customer_list.append(CustomerDB(**customer, id=customer['_id']))

        return customer_list

    async def get_customer(self, customer_id: OID) -> CustomerDB:
        customer_q = await self.db.customer_tb.find_one({'_id': ObjectId(customer_id)})
        if customer_q:
            return CustomerDB(**customer_q, id=customer_q['_id'])

    async def delete_customer(self, customer_id: OID):
        await self.db.customer_tb.delete_one({'_id': ObjectId(customer_id)})

    async def update_customer(self, customer_id: OID, customer: CustomerDB):
        await self.db.customer_tb.update_one({'_id': ObjectId(customer_id)},
                                             {'$set': customer.dict(exclude={'id'})})

    async def add_customer(self, customer: CustomerDB):
        await self.db.customer_tb.insert_one(customer.dict(exclude={'id'}))
