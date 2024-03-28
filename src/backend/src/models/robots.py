from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from schemas.robots import RobotCreate

Base = declarative_base()


class Robot(Base):
    __tablename__ = "robots"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    route = Column(String, index=True)

    @classmethod
    async def create(cls, db_session: Session, robot_data: RobotCreate):
        robot = cls(name=robot_data.name, route=robot_data.route)
        db_session.add(robot)
        db_session.commit()
        db_session.refresh(robot)
        return robot

    @classmethod
    async def read_all(cls, db_session: Session):
        return db_session.query(cls).all()

    @classmethod
    async def read(cls, db_session: Session, robot_id: int):
        return db_session.query(cls).filter(cls.id == robot_id).first()

    @classmethod
    async def update(cls, db_session: Session, robot_id: int, robot_data: RobotCreate):
        robot = db_session.query(cls).filter(cls.id == robot_id).first()
        if robot:
            robot.name = robot_data.name
            robot.route = robot_data.route
            db_session.commit()
            db_session.refresh(robot)
        return robot

    @classmethod
    async def delete(cls, db_session: Session, robot_id: int):
        robot = db_session.query(cls).filter(cls.id == robot_id).first()
        if robot:
            db_session.delete(robot)
            db_session.commit()
            return True
        return False
