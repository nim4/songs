from flask import jsonify, request
from songs import app, songs_collection, ratings_collection
from songs.models import Song, Rating


@app.route("/songs", methods=["GET"])
def get_songs():
    skip = request.args.get("page", default=0, type=int)
    limit = request.args.get("per_page", default=10, type=int)

    # Set maximum limit size
    limit = min(10, limit)

    songs = list(map(lambda s: Song(s).to_dict(), songs_collection.find().skip(skip * limit).limit(limit)))
    return jsonify({"songs": songs})


@app.route("/songs/avg/difficulty", methods=["GET"])
def get_with_difficulty_level():
    level = request.args.get("level", default=0, type=int)

    query = []
    if level > 0:
        query.append({"$match": {"level": level}})

    query.append({"$group": {"avg": {"$avg": "$difficulty"}, "_id": ""}})

    try:
        data = list(songs_collection.aggregate(query))[0]
        return jsonify({"avg_difficulty": data["avg"]})
    except IndexError:
        return "", 404


@app.route("/songs/search", methods=["GET"])
def search_songs():
    message = request.args.get("message", default="", type=str)

    songs = list(map(lambda s: Song(s).to_dict(), songs_collection.find(
        {"$text": {"$search": message}},
        {"score": {"$meta": "textScore"}}).sort([("score", {"$meta": "textScore"})])))
    return jsonify(songs)


@app.route("/songs/rating", methods=["POST"])
def add_rating():
    try:
        rating = Rating(request.get_json())
        inserted = ratings_collection.insert_one(rating.to_dict())
        response = jsonify({"rating_id": str(inserted.inserted_id)})
        return response, 201
    except KeyError or ValueError:
        return "", 400


@app.route("/songs/avg/rating/<song_id>", methods=["GET"])
def get_rating(song_id):
    query = [{"$group": {"avg": {"$avg": "$rating"}, "_id": song_id}}]

    try:
        data = list(ratings_collection.aggregate(query))[0]
        return jsonify({"avg_difficulty": data["avg"]})
    except IndexError:
        return "", 404
