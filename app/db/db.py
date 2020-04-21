from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.config import Config, config

global session, engine


def init_db(environment="default"):
    SQLALCHEMY_DATABASE_URL = config[environment]().DB_CONNECTION
    # SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

    global engine
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL
    )

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    global session
    session = SessionLocal

    return session, engine