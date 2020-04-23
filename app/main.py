from fastapi import FastAPI

from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session


def create_app(session: Session, engine: Engine, environment="default"):
    # config[environment].db = session
    app = FastAPI()

    # TODO: Figure out if there is a better way to do this with DI
    from app.routers import api
    app.include_router(api.router)

    return app
