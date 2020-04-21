import os

from app.db.db import init_db
from app.main import create_app

session, engine = init_db(os.getenv('ENVIRONMENT') or 'default')
app = create_app(session, engine, os.getenv('ENVIRONMENT') or 'default')
