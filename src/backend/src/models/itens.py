from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from schemas.itens import ItemCreate

Base = declarative_base()


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    @classmethod
    async def create(cls, db_session: Session, item_data: ItemCreate):
        item = Item(name=item_data.name)
        db_session.add(item)
        db_session.commit()
        db_session.refresh(item)
        return item

    @classmethod
    async def read(cls, db_session: Session, item_id: int):
        return db_session.query(Item).filter(Item.id == item_id).first()

    @classmethod
    async def read_all(cls, db_session: Session):
        return db_session.query(cls).all()

    @classmethod
    async def update(cls, db_session: Session, item_id: int, item_data: ItemCreate):
        item = db_session.query(Item).filter(Item.id == item_id).first()
        if item:
            item.name = item_data.name
            db_session.commit()
            db_session.refresh(item)
            return item
        return None

    @classmethod
    async def delete(cls, db_session: Session, item_id: int):
        item = db_session.query(Item).filter(Item.id == item_id).first()
        if item:
            db_session.delete(item)
            db_session.commit()
            return True
        return False
