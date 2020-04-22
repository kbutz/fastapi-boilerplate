from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from alembic.config import Config as AlembicConfig
from alembic import command

from app.db import models
from config.config import Config, config

global session


def init_db(environment="default"):
    SQLALCHEMY_DATABASE_URL = config[environment]().DB_CONNECTION
    # SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL
    )

    # models.Base.metadata.create_all(bind=engine)

    alembic_cfg = AlembicConfig("./app/alembic.ini")
    command.upgrade(alembic_cfg, "head")

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    global session
    session = SessionLocal

    return session, engine