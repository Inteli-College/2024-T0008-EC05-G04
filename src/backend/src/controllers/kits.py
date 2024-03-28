from sqlalchemy.orm import Session
from models.kits import Kit


class KitController:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create(self, kit_data):
        return await Kit.create(self.db_session, kit_data)

    async def get_all(self):
        return await Kit.read_all(self.db_session)

    async def get(self, kit_id: int):
        return await Kit.read(self.db_session, kit_id)

    async def update(self, kit_id: int, kit_data):
        return await Kit.update(self.db_session, kit_id, kit_data)

    async def delete(self, kit_id: int):
        return await Kit.delete(self.db_session, kit_id)
