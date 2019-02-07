from songs import ratings_collection


class RatingRepository:
    @staticmethod
    def create(rating):
        inserted = ratings_collection.insert_one(rating.to_dict())
        return str(inserted.inserted_id)

    @staticmethod
    def get_song_avg_rating(song_id):
        query = [{"$group": {"avg": {"$avg": "$rating"}, "_id": song_id}}]

        try:
            data = list(ratings_collection.aggregate(query))[0]
            return data["avg"]
        except IndexError:
            return None
