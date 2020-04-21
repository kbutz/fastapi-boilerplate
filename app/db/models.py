from datetime import datetime

from sqlalchemy import Column, Integer, String, TEXT, TIMESTAMP
from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from app.db import db

Base = declarative_base()


class ApiLogBase(BaseModel):
    payload: str


class ApiLogCreate(ApiLogBase):
    id: int

    class Config:
        orm_mode = True


class ApiLog(Base):
    __tablename__ = 'api_logs'
    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP, default=datetime.now())
    endpoint = Column(String(100))
    payload = Column(TEXT)

    def create_api_log(self, session: Session, api_log: ApiLogCreate):
        new_api_log = ApiLog(payload=api_log.payload)
        try:
            session.add(new_api_log)
            session.commit()
            session.refresh(new_api_log)
        except Exception as e:
            print(e)
            session.rollback()

        return new_api_log
