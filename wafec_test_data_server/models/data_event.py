from .base import Base

from sqlalchemy import Column, Integer, String


class DataEvent(Base):
    __tablename__ = 'DATA_EVENT'

    id = Column(Integer, primary_key=True)
    source = Column(String)
    event_name = Column(String)
    value = Column(String)
