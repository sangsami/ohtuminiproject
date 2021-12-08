# from app import db
# # pylint: disable=no-member
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True)
    password = Column(String(100))
    time_created = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self) -> str:
        return f"<User(username={self.username}, time_created={self.time_created})>"
