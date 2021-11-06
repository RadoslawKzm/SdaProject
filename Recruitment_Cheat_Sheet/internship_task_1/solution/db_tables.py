from db_connector import Base
from sqlalchemy import Column, Integer, String, Float


# class ReprClass:
#     def __repr__(self):
#         return f"""name={self.__tablename__},
#         {','.join(f'{k}={v}' for k, v in self.__dict__.items() if not k.startswith('_'))}"""
#

class Movies(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(String)
    runtime = Column(String)
    genre = Column(String)
    director = Column(String)
    actors = Column(String)
    writer = Column(String)
    language = Column(String)
    country = Column(String)
    awards = Column(String)
    imdb_rating = Column(String)
    imdb_votes = Column(String)
    box_office = Column(String)
