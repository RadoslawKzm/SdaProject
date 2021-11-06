from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

Base = declarative_base()


class DbContext(sessionmaker):
    """
    Context manager class for managing SQLalchemy session objects.
    It manages opening transactions, returns session object then after transaction commits/rollbacks and closes.
    It manages all fallbacks for user.
    User doesn't need to worry about commiting changes to DB and exception handling.
    """

    def __init__(self, *args, suppress: bool = False, **kwargs):
        super(DbContext, self).__init__(*args, **kwargs)
        self.suppress = suppress

    def __enter__(self) -> Session:
        """
        :return: SQLalchemy session object for context manager to operate on.
        """
        self.session = self()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if any((exc_type, exc_val, exc_tb)):
            self.session.rollback()
            self.session.close()
            self.json = {"exc_type": str(exc_type), "exc_val": str(exc_val), "exc_tb": str(exc_tb)}
            return self.suppress  # gracefully suppressing
        self.session.commit()
        self.session.close()

    @staticmethod
    def get_engine():
        """
        Simple function for getting SQLalchemy engine object
        :return: SQLalchemy engine object with established connection
        """
        POSTGRES_USER = "postgres"
        POSTGRES_PASSWORD = "changeme"
        POSTGRES_HOSTNAME = "localhost"
        POSTGRES_DB = "db"
        return create_engine(
            f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOSTNAME}/{POSTGRES_DB}"
        )
