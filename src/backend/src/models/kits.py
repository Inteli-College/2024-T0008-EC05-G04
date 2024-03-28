from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from schemas.kits import KitCreate

Base = declarative_base()


class Kit(Base):
    __tablename__ = "kits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    @classmethod
    async def create(cls, db_session: Session, kit_data: KitCreate):
        kit = cls(name=kit_data.name)
        db_session.add(kit)
        db_session.commit()
        db_session.refresh(kit)
        return kit

    @classmethod
    async def read_all(cls, db_session: Session):
        return db_session.query(cls).all()

    @classmethod
    async def read(cls, db_session: Session, kit_id: int):
        return db_session.query(cls).filter(cls.id == kit_id).first()

    @classmethod
    async def update(cls, db_session: Session, kit_id: int, kit_data: KitCreate):
        kit = db_session.query(cls).filter(cls.id == kit_id).first()
        if kit:
            kit.name = kit_data.name
            db_session.commit()
            db_session.refresh(kit)
            return kit
        return None

    @classmethod
    async def delete(cls, db_session: Session, kit_id: int):
        kit = db_session.query(cls).filter(cls.id == kit_id).first()
        if kit:
            db_session.delete(kit)
            db_session.commit()
            return True
        return False
