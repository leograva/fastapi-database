from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import items
from schemas import ItemCreate
from database import database

async def create_item(item: ItemCreate):
    query = items.insert().values(name=item.name, description=item.description)
    last_record_id = await database.execute(query)
    return {**item.dict(), "id": last_record_id}

async def get_item(item_id: int):
    query = select(items).where(items.c.id == item_id)
    return await database.fetch_one(query)

async def get_items():
    query = select(items)
    return await database.fetch_all(query)

async def update_item(item_id: int, item: ItemCreate):
    query = items.update().where(items.c.id == item_id).values(name=item.name, description=item.description)
    await database.execute(query)
    return {**item.dict(), "id": item_id}

async def delete_item(item_id: int):
    query = items.delete().where(items.c.id == item_id)
    await database.execute(query)
