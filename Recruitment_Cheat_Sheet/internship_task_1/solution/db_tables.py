from db_connector import Base
from sqlalchemy import Column, Integer, String, Float


class Movies(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    runtime = Column(String)
    genre = Column(String)
    director = Column(String)
    actors = Column(String)
    writer = Column(String)
    language = Column(String)
    country = Column(String)
    awards = Column(String)
    imdb_rating = Column(Float)
    imdb_votes = Column(String)
    box_office = Column(String)
