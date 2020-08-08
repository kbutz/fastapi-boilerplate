import time
from datetime import datetime

from fastapi import APIRouter, BackgroundTasks, Depends
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


# TODO: Fix import cycle here
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
def example_route_get(db: Session = Depends(get_db)):
    # Example DB transaction w/ sql-alchemy
    request_transaction = ApiLog(
        endpoint="TODO",
        payload="str(item)"
    )

    request_transaction.create_api_log(db, request_transaction)
    return {"hello": "world"}

"""Async example, showing how to kick off background tasks"""
def write_notification(date: datetime):
    time.sleep(1)
    print(date)

@router.get("/async-task")
async def async_task_example(background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, datetime.now())
    return {"message": "Notification sent in the background"}
