from sqlalchemy import Column, String
# from sqlalchemy.ext.declarative import declarative_base

from PythonSemiAdvanced.day_2.task_3 import Base

class BaseTable(Base):
    __tablename__ = "base_table"
    __table_args__ = {'schema': 'test_schema'}
    CURRENCY = Column(String)
    FIRST_NAME = Column(String)
    LETTERS_IN_NAME = Column(String)
    LAST_NAME = Column(String)
    REVERTED_LAST_NAME = Column(String)
    EMAIL = Column(String)
    AGE = Column(String)
    BIRTHDAY = Column(String)
    NATIONALITY = Column(String)
    LOGIN = Column(String)
    PASSWORD = Column(String)
    CITY = Column(String)
    STREET = Column(String)
    NUMBER = Column(String)
    COUNTRY = Column(String)