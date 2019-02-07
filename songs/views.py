from flask import jsonify, request
from songs import app
from songs.repositories import SongRepository, RatingRepository
from songs.models import Rating


@app.route("/songs", methods=["GET"])
def get_songs():
    skip = request.args.get("page", default=0, type=int)
    limit = request.args.get("per_page", default=10, type=int)
    songs = SongRepository.get_songs(skip, limit)
    return jsonify({"songs": songs})


@app.route("/songs/avg/difficulty", methods=["GET"])
def get_with_difficulty_level():
    level = request.args.get("level", default=0, type=int)

    avg = SongRepository.get_difficulty_by_level(level)
    if avg is None:
        return "", 404

    return jsonify({"avg_difficulty": avg})


@app.route("/songs/search", methods=["GET"])
def search_songs():
    message = request.args.get("message", default="", type=str)

    songs = SongRepository.search(message)
    return jsonify({"songs": songs})


@app.route("/songs/rating", methods=["POST"])
def add_rating():
    try:
        rating = Rating(request.get_json())
        rating_id = RatingRepository.create(rating)
        return jsonify({"rating_id": rating_id}), 201
    except KeyError or ValueError:
        return "", 400


@app.route("/songs/avg/rating/<song_id>", methods=["GET"])
def get_rating(song_id):
    avg_rating = RatingRepository.get_song_avg_rating(song_id)
    if avg_rating is None:
        return "", 404

    return jsonify({"avg_rating": avg_rating})
