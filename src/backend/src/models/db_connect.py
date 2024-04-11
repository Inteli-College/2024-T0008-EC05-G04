from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tokens import (
    DATABASE_URL,
)  # Garanta que esteja apontando para seu arquivo tokens.py correto

# Importando Base e modelos
from models.base import Base
from models.itens import Item
from models.kits import Kit
from models.kit_positions import KitPosition
from models.kit_orders import KitOrder

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_database():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_database()
