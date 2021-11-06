from typing import Dict

import requests
import pandas as pd
from output import output_short

from db_connector import Base, DbContext
from db_tables import Movies


class Movie:
    movies = []

    def __init__(self, input_dict: Dict[str, str]):
        self.title = input_dict["Title"]
        self.year = input_dict["Year"]
        self.runtime = input_dict["Runtime"]
        self.genre = input_dict["Genre"]
        self.director = input_dict["Director"]
        self.actors = input_dict["Actors"]
        self.writer = input_dict["Writer"]
        self.language = input_dict["Language"]
        self.country = input_dict["Country"]
        self.awards = input_dict["Awards"]
        self.imdb_rating = input_dict["imdbRating"]
        self.imdb_votes = input_dict["imdbVotes"]
        self.box_office = input_dict.get("BoxOffice", "")
        self.update_movies()

    def update_movies(self):
        self.movies.append(self.__dict__)


def get_movies_from_omdb():
    titles = list(pd.read_csv("movies.csv")["title"])
    output = [requests.get(f"https://www.omdbapi.com/?t={title}&plot=full&&apikey=15c2b5b5").json() for title in titles]
    with open("output_long.py", "w") as file:
        file.write(f"output={str(output)}")


def populate_csv():
    """populate new_movies.csv with data"""
    # lst = []
    # for m in output_short:
    #     new_dict = {"title": m["Title"], "runtime": m["Runtime"], "genre": m["Genre"],
    #                 "director": m["Director"], "cast": m["Actors"], "writer": m["Writer"], "language": m["Language"],
    #                 "country": m["Country"], "awards": m["Awards"], "imdb_rating": m["imdbRating"],
    #                 "imdb_votes": m["imdbVotes"], "box_office": m.get("BoxOffice", "")}
    #     lst.append(new_dict)
    # pd.DataFrame(lst).to_csv("new_movies.csv", index_label="id")
    for movie_dict in output_short:
        Movie(movie_dict)
    pd.DataFrame(Movie.movies).to_csv("new_movies_2.csv", index_label="id")

    with DbContext(bind=DbContext.get_engine()) as session:
        # for movie in Movie.movies:
        #     session.add(Movies(**movie))
        session.add_all([Movies(**movie) for movie in Movie.movies])


if __name__ == '__main__':
    # get_movies_from_omdb()
    Base.metadata.create_all(DbContext.get_engine())
    populate_csv()
