class Rating:
    def __init__(self, dictionary):
        self.song_id = dictionary["song_id"]
        self.rating = dictionary["rating"]
        if not (0 <= self.rating <= 5):
            raise ValueError

    def to_dict(self):
        return self.__dict__
