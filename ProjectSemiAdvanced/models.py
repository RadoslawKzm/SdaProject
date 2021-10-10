from uuid import uuid4

from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID

from ProjectSemiAdvanced.db_connector import Base


class BaseTable(Base):
    __tablename__ = "base_table"

    UUID = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    GENDER = Column(String)
    FIRST_NAME = Column(String)
    LAST_NAME = Column(String)
    EMAIL = Column(String)
    AGE = Column(Integer)
    BIRTHDAY = Column(String)
    NATIONALITY = Column(String)
    LOGIN = Column(String)
    PASSWORD = Column(String)
    CITY = Column(String)
    STREET = Column(String)
    NUMBER = Column(Integer)
    COUNTRY = Column(String)
