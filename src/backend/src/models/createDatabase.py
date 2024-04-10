from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from tokens import DATABASE_URL

# Substitua esta string pela sua string de conexão real

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)

Base = declarative_base()

# Importe seus modelos aqui. Substitua `your_model_directory` pelo nome do diretório onde seus modelos estão localizados
from .itens import Item
from .kits import Kit
from .kit_positions import KitPosition
from .kit_orders import KitOrder
from .robots import Robot


def create_database():
    # Cria as tabelas no banco de dados
    Base.metadata.create_all(bind=engine)
    print("haha")
