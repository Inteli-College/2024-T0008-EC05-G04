from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from datetime import datetime
from schemas.kit_orders import KitOrderCreate

from .kits import Kit
from .robots import Robot

Base = declarative_base()


class KitOrder(Base):
    __tablename__ = "kit_orders"

    id = Column(Integer, primary_key=True, index=True)
    robot_id = Column(Integer, ForeignKey("robots.id"))
    status = Column(String, index=True)
    kit_id = Column(Integer, ForeignKey("kits.id"))
    start_date = Column(DateTime, default=datetime.now())
    end_date = Column(DateTime, nullable=True)
    requested_by = Column(Integer, ForeignKey("users.id"))

    robot = relationship(Robot, back_populates="kit_orders")
    kit = relationship(Kit, back_populates="kit_orders")

    @classmethod
    async def create(cls, db_session: Session, kit_order_data: KitOrderCreate):
        kit_order = cls(
            robot_id=kit_order_data.robot_id,
            kit_id=kit_order_data.kit_id,
            requested_by=kit_order_data.requested_by,
        )
        db_session.add(kit_order)
        db_session.commit()
        db_session.refresh(kit_order)
        return kit_order

    @classmethod
    async def read_all(cls, db_session: Session):
        return db_session.query(cls).all()

    @classmethod
    async def read(cls, db_session: Session, kit_order_id: int):
        return db_session.query(cls).filter(cls.id == kit_order_id).first()

    @classmethod
    async def update(cls, db_session: Session, kit_order_id: int, **kwargs):
        kit_order = db_session.query(cls).filter(cls.id == kit_order_id).first()
        if kit_order:
            for key, value in kwargs.items():
                setattr(kit_order, key, value)
            db_session.commit()
            db_session.refresh(kit_order)
        return kit_order

    @classmethod
    async def delete(cls, db_session: Session, kit_order_id: int):
        kit_order = db_session.query(cls).filter(cls.id == kit_order_id).first()
        if kit_order:
            db_session.delete(kit_order)
            db_session.commit()
            return True
        return False
