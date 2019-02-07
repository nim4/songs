from flask import Flask
from pymongo import MongoClient, TEXT

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)
db = MongoClient('localhost:27017').yousician
songs_collection = db.songs
ratings_collection = db.ratings

db.songs.create_index([("artist", TEXT), ("title", TEXT)])

import songs.views
