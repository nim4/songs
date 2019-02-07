from songs import songs_collection
from songs.models import Song


class SongRepository:
    @staticmethod
    def get_songs(skip, limit):
        # Set maximum limit size
        limit = min(10, limit)

        return list(map(lambda s: Song(s).to_dict(), songs_collection.find().skip(skip * limit).limit(limit)))

    @staticmethod
    def get_difficulty_by_level(level):
        query = []
        if level > 0:
            query.append({"$match": {"level": level}})

        query.append({"$group": {"avg": {"$avg": "$difficulty"}, "_id": ""}})

        try:
            data = list(songs_collection.aggregate(query))[0]
            return data["avg"]
        except IndexError:
            return None

    @staticmethod
    def search(message):
        songs = list(map(lambda s: Song(s).to_dict(), songs_collection.find(
            {"$text": {"$search": message}},
            {"score": {"$meta": "textScore"}}).sort([("score", {"$meta": "textScore"})])))
        return songs
