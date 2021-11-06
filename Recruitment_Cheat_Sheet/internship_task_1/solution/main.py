import requests
import pandas as pd
from output import output_short


class Movie:
    movies = []

    def __init__(self, dictio):
        self.title = dictio["Title"]
        self.year = dictio["Year"]
        self.runtime = dictio["Runtime"]
        self.genre = dictio["Genre"]
        self.director = dictio["Director"]
        self.actors = dictio["Actors"]
        self.writer = dictio["Writer"]
        self.language = dictio["Language"]
        self.country = dictio["Country"]
        self.awards = dictio["Awards"]
        self.imdb_rating = dictio["imdbRating"]
        self.imdb_votes = dictio["imdbVotes"]
        self.box_office = dictio.get("BoxOffice", "")
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
        movie = Movie(movie_dict)
    pd.DataFrame(Movie.movies).to_csv("new_movies_2.csv")


if __name__ == '__main__':
    # get_movies_from_omdb()
    populate_csv()
