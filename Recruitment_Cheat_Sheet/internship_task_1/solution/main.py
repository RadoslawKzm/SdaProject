import requests
import csv
import pandas as pd


def get_movies_from_omdb():
    titles = list(pd.read_csv("movies.csv")["title"])
    output = [requests.get(f"https://www.omdbapi.com/?t={title}&plot=full&&apikey=15c2b5b5").json() for title in titles]
    with open("output_long.py", "w") as file:
        file.write(f"output={str(output)}")


if __name__ == '__main__':
    dummy()
