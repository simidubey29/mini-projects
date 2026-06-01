import json
import os

FILE_PATH = "library.json"


def load_books():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as file:
        return json.load(file)


def save_books(books):
    with open(FILE_PATH, "w") as file:
        json.dump(books, file, indent=4)