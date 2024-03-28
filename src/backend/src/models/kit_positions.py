from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from schemas.kit_positions import KitPositionCreate

from .kits import Kit
from .itens import Item

Base = declarative_base()


class KitPosition(Base):
    __tablename__ = "kit_positions"

    id = Column(Integer, primary_key=True, index=True)
    kit_id = Column(Integer, ForeignKey("kits.id"))
    position = Column(Integer)
    item_id = Column(Integer, ForeignKey("items.id"))

    kit = relationship(Kit, back_populates="kit_positions")
    item = relationship(Item, back_populates="kit_positions")

    @classmethod
    async def create(cls, db_session: Session, kit_position_data: KitPositionCreate):
        kit_position = cls(
            kit_id=kit_position_data.kit_id,
            position=kit_position_data.position,
            item_id=kit_position_data.item_id,
        )
        db_session.add(kit_position)
        db_session.commit()
        db_session.refresh(kit_position)
        return kit_position

    @classmethod
    async def read_all(cls, db_session: Session):
        return db_session.query(cls).all()

    @classmethod
    async def read(cls, db_session: Session, kit_position_id: int):
        return db_session.query(cls).filter(cls.id == kit_position_id).first()

    @classmethod
    async def update(cls, db_session: Session, kit_position_id: int, **kwargs):
        kit_position = db_session.query(cls).filter(cls.id == kit_position_id).first()
        if kit_position:
            for key, value in kwargs.items():
                setattr(kit_position, key, value)
            db_session.commit()
            db_session.refresh(kit_position)
        return kit_position

    @classmethod
    async def delete(cls, db_session: Session, kit_position_id: int):
        kit_position = db_session.query(cls).filter(cls.id == kit_position_id).first()
        if kit_position:
            db_session.delete(kit_position)
            db_session.commit()
            return True
        return False
