from sqlalchemy.orm import Session
from models.kit_positions import KitPosition


class KitPositionController:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create(self, kit_position_data):
        return await KitPosition.create(self.db_session, kit_position_data)

    async def get_all(self):
        return await KitPosition.read_all(self.db_session)

    async def get(self, kit_position_id: int):
        return await KitPosition.read(self.db_session, kit_position_id)

    async def update(self, kit_position_id: int, **kwargs):
        return await KitPosition.update(self.db_session, kit_position_id, **kwargs)

    async def delete(self, kit_position_id: int):
        return await KitPosition.delete(self.db_session, kit_position_id)
