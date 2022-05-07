
from abc import abstractmethod
from typing import List

from src.db.models import CustomerDB, OID


class DatabaseManager(object):
    @property
    def client(self):
        raise NotImplementedError

    @property
    def db(self):
        raise NotImplementedError

    @abstractmethod
    async def connect_to_database(self, path: str):
        pass

    @abstractmethod
    async def close_database_connection(self):
        pass

    @abstractmethod
    async def get_customers(self) -> List[CustomerDB]:
        pass

    @abstractmethod
    async def get_customer(self, customer_id: OID) -> CustomerDB:
        pass

    @abstractmethod
    async def add_customer(self, customer: CustomerDB):
        pass

    @abstractmethod
    async def update_customer(self, customer_id: OID, post: CustomerDB):
        pass

    @abstractmethod
    async def delete_customer(self, customer_id: OID):
        pass
