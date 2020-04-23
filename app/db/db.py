from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from alembic.config import Config as AlembicConfig
from alembic import command

from config.config import config

global session


def init_db(environment="default"):
    SQLALCHEMY_DATABASE_URL = config[environment]().DB_CONNECTION
    # SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL
    )

    # TODO: Soe schools of thought on DB migrations say run the create_all first for setting up an up-to-date local
    #       environment in one command instead of iterating through all the migration versions. Laving this here
    #       incase I want to do that. Personally, I'd like to treat local dev like prod, where create_all will never run.
    # models.Base.metadata.create_all(bind=engine)

    alembic_cfg = AlembicConfig("./app/alembic.ini")
    alembic_cfg.set_main_option("sqlalchemy.url", config[environment]().DB_CONNECTION)
    command.upgrade(alembic_cfg, "head")

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    global session
    session = SessionLocal

    # TODO: These return values aren't being used, but I'd like to use them over fastapi's dependency injection pattern
    #       as a way to provide the DB connection
    return session, engine
