from fastapi import APIRouter
from endpoints.allKits import app as allKits
from endpoints.addKits import app as addKits
from endpoints.resgister import app as register
from endpoints.login import app as login
from endpoints.kitPositionCreate import app as kitPositionCreate
from endpoints.inserItem import app as inserItem
from endpoints.allKitPositions import app as allKitPositions
from endpoints.itens import app as itens
from endpoints.kitOrderCreate import app as kitOrderCreate
from endpoints.kitsOrder import app as kitsOrder
from endpoints.orderAtt import app as orderAtt
from endpoints.execute import app as execute

app = APIRouter()
app.include_router(allKits)
app.include_router(addKits)
app.include_router(register)
app.include_router(login)
app.include_router(kitPositionCreate)
app.include_router(inserItem)
app.include_router(allKitPositions)
app.include_router(itens)
app.include_router(kitOrderCreate)
app.include_router(kitsOrder)
app.include_router(orderAtt)
app.include_router(execute)
