from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .base import Base
from .data_event import DataEvent

__all__ = [
    'Session',
    'engine',
    'DataEvent'
]


engine = create_engine('mysql+pymysql://data_test:data_test-321@localhost/data_test')

Session = sessionmaker(bind=engine)
