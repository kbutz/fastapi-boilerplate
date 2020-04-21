from fastapi import APIRouter, Depends
from pydantic import BaseModel

from sqlalchemy.orm import Session

from app.db.db import session
from app.db.models import ApiLog

router = APIRouter()


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


# TODO: Import cycle here
# Dependency
def get_db():
    try:
        db = session()
        yield db
    finally:
        db.close()


# Example route
@router.post('/example-route')
def example_route_post(db: Session = Depends(get_db)):
    # Example DB transaction w/ sql-alchemy
    request_transaction = ApiLog(endpoint="TODO",
                                 payload="str(item)")

    request_transaction.create_api_log(db, request_transaction)

    return {"success": "ok", "message": "item: Item -> item.description"}


@router.get('/example-route')
def example_route_get():
    return {"hello": "world"}
