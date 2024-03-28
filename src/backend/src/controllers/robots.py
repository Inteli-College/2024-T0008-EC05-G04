from sqlalchemy.orm import Session
from models.robots import Robot


class RobotController:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def create(self, robot_data):
        return await Robot.create(self.db_session, robot_data)

    async def get_all(self):
        return await Robot.read_all(self.db_session)

    async def get(self, robot_id: int):
        return await Robot.read(self.db_session, robot_id)

    async def update(self, robot_data):
        return await Robot.update(self.db_session, robot_data)

    async def delete(self, robot_id: int):
        return await Robot.delete(self.db_session, robot_id)
