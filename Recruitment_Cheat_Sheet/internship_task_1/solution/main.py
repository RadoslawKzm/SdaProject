import requests
import pandas as pd
from output import output_short


def get_movies_from_omdb():
    titles = list(pd.read_csv("movies.csv")["title"])
    output = [requests.get(f"https://www.omdbapi.com/?t={title}&plot=full&&apikey=15c2b5b5").json() for title in titles]
    with open("output_long.py", "w") as file:
        file.write(f"output={str(output)}")


def populate_csv():
    """populate new_movies.csv with data"""
    lst = []
    for m in output_short:
        new_dict = {"title": m["Title"], "runtime": m["Runtime"], "genre": m["Genre"],
                    "director": m["Director"], "cast": m["Actors"], "writer": m["Writer"], "language": m["Language"],
                    "country": m["Country"], "awards": m["Awards"], "imdb_rating": m["imdbRating"],
                    "imdb_votes": m["imdbVotes"], "box_office": m.get("BoxOffice", "")}
        lst.append(new_dict)
    pd.DataFrame(lst).to_csv("new_movies.csv", index_label="id")


if __name__ == '__main__':
    # get_movies_from_omdb()
    populate_csv()
