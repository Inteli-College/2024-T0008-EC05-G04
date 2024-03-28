from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tokens import DATABASE_URL
from . import (
    itens,
    kits,
    kit_orders,
    kit_positions,
    robots
)


engine = create_engine(DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = Session()

itens_controller = itens.ItemController(session)
kits_controller = kits.KitController(session)
kit_orders_controller = kit_orders.KitOrderController(session)
kit_positions_controller = kit_positions.KitPositionController(session)
robots_controller = robots.RobotController(session)
