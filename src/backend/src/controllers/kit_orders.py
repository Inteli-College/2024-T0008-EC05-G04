from sqlalchemy.orm import Session
from models.kit_orders import KitOrder


class KitOrderController:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create(self, kit_order_data):
        return await KitOrder.create(self.db_session, kit_order_data)

    async def get_all(self):
        return await KitOrder.read_all(self.db_session)

    async def get(self, kit_order_id: int):
        return await KitOrder.read(self.db_session, kit_order_id)

    async def update(self, kit_order_id: int, **kwargs):
        return await KitOrder.update(self.db_session, kit_order_id, **kwargs)

    async def delete(self, kit_order_id: int):
        return await KitOrder.delete(self.db_session, kit_order_id)
