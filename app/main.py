from fastapi import FastAPI

# from app.db import db
# from config.config import config
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from app.db import models


def create_app(session: Session, engine: Engine, environment="default"):
    # config[environment].db = session
    # TODO: Use migrations here
    models.Base.metadata.create_all(bind=engine)

    app = FastAPI()

    # TODO: Figure out if there is a better way to do this with DI
    from app.routers import api
    app.include_router(api.router)

    return app
