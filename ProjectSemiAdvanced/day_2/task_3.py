from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from ProjectSemiAdvanced.day_2.task_3_table import BaseTable

Base = declarative_base()


def get_engine():
    """
    Simple function for getting SQLalchemy engine object
    :return: SQLalchemy engine object with established connection
    """
    POSTGRES_USER = "postgres"
    POSTGRES_PASSWORD = "changeme"
    POSTGRES_HOSTNAME = "localhost"
    PORT = 5432
    POSTGRES_DB = "db"
    return create_engine(
        f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOSTNAME}/{POSTGRES_DB}"
    )


Base.metadata.create_all(get_engine())
Session = sessionmaker(bind=get_engine())
session = Session()
"""cos zrobic"""
session.commit()
session.close()
