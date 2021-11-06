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


if __name__ == '__main__':
    # get_movies_from_omdb()
    populate_csv()
