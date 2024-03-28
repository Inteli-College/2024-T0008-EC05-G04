from sqlalchemy.orm import Session
from models.itens import Item


class ItemController:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create(self, item_data):
        return await Item.create(self.db_session, item_data)

    async def get_all(self):
        return await Item.read_all(self.db_session)

    async def get(self, item_id: int):
        return await Item.read(self.db_session, item_id)

    async def update(self, item_id: int, item_data):
        return await Item.update(self.db_session, item_id, item_data)

    async def delete(self, item_id: int):
        return await Item.delete(self.db_session, item_id)
