import json
import os
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session


class Config:
    def __init__(self):
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        self.SQLALCHEMY_ECHO = False
        self.db: Optional[Session] = None
        self.DB_CONNECTION = ""

    # Optional method to implement in sub-classes. Can be called to perform any environment dependent initialization
    @staticmethod
    def init_app(app):
        pass


# Example Development config loading configuration variables from file
class DevelopmentConfig(Config):
    def __init__(self):
        print("!!!!!!!!!!!!")
        Config.__init__(self)
        self.DEBUG = True
        self.SQLALCHEMY_ECHO = True

        config_path = "./config/local_settings.json"

        with open(config_path, 'r') as config_json:
            print("????????????")
            config_settings = json.load(config_json)

            self.MYSQL_DRIVER = config_settings["db_driver"]
            self.MYSQL_PORT = config_settings["db_port"]

            self.MYSQL_HOST = config_settings["db_host"]
            self.MYSQL_USER = config_settings["db_user"]
            self.MYSQL_PASS = config_settings["db_pass"]

            self.EXAMPLE_DB = config_settings["example_db"]

            self.DB_CONNECTION = self.MYSQL_DRIVER \
                                   + "://" + self.MYSQL_USER \
                                   + ":" + self.MYSQL_PASS \
                                   + "@" + self.MYSQL_HOST \
                                   + ":" + self.MYSQL_PORT \
                                   + "/" + self.EXAMPLE_DB

            print(self.DB_CONNECTION)
            # Default Database URI
            self.SQLALCHEMY_DATABASE_URI = self.DB_CONNECTION
            # Optionally define multiple sql-alchemy binds to handle multiple connections
            # self.SQLALCHEMY_BINDS = {
            #     "write_connection": self.DB_CONNECTION_1,
            #     "read_connection": self.DB_CONNECTION_2
            # }

            # self.engine = create_engine(
            #     self.SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False}
            # )
            #
            # self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
            #
            # self.Base = declarative_base()


# Example test config, running the app with a sqlite DB
class UnitTestConfig(Config):
    def __init__(self):
        Config.__init__(self)
        self.DEBUG = True
        self.SQLALCHEMY_ECHO = True
        self.SQLALCHEMY_DB_URI = 'sqlite:///:memory:'


# Example production config setting configuration variables from environment variables
class ProductionConfig(Config):
    def __init__(self):
        Config.__init__(self)
        self.MYSQL_DRIVER = os.getenv("db_driver")
        self.MYSQL_PORT = os.getenv("db_port")

        self.MYSQL_HOST = os.getenv("db_host")
        self.MYSQL_USER = os.getenv("db_user")
        self.MYSQL_PASS = os.getenv("db_pass")

        self.EXAMPLE_DB = os.getenv("example_db")

        self.DB_CONNECTION = self.MYSQL_DRIVER \
                               + "://" + self.MYSQL_USER \
                               + ":" + self.MYSQL_PASS \
                               + "@" + self.MYSQL_HOST \
                               + ":" + self.MYSQL_PORT \
                               + "/" + self.EXAMPLE_DB

        # Default Database URI
        self.SQLALCHEMY_DATABASE_URI = self.DB_CONNECTION

        self.SQLALCHEMY_ENGINE_OPTIONS = {
            'echo_pool': False,  # Set to True or 'debug' to log useful pool events for debugging
            'pool_pre_ping': True,
            'pool_timeout': 30,
            # 'pool_recycle': 3600,  # Defaults to none, waits for mysql to disconnect after 8 hours of inactivity
            'connect_args': {'connect_timeout': 5, 'read_timeout': 5, 'write_timeout': 5}
        }


config = {
    'development': DevelopmentConfig,
    'testing': UnitTestConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
