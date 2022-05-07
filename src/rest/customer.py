from fastapi import APIRouter, Depends

from src.db import DatabaseManager, get_database
from src.db.models import CustomerDB, OID

router = APIRouter()


@router.get('/')
async def get_all(db: DatabaseManager = Depends(get_database)):
    customers = await db.get_customers()
    return customers


@router.post('/', status_code=201)
async def create(customer: CustomerDB, db: DatabaseManager = Depends(get_database)):
    customer = await db.add_customer(customer)
    return customer


@router.get('/{customer_id}')
async def get(customer_id: OID, db: DatabaseManager = Depends(get_database)):
    post = await db.get_customer(customer_id=customer_id)
    return post


@router.put('/{customer_id}')
async def get(post_id: OID, post: CustomerDB, db: DatabaseManager = Depends(get_database)):
    post = await db.update_customer(post=post, post_id=post_id)
    return post


@router.delete('/{customer_id}')
async def delete(customer_id: OID, db: DatabaseManager = Depends(get_database)):
    await db.delete_customer(customer_id=customer_id)
