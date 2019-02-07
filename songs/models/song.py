class Song:
    def __init__(self, dictionary):
        self.artist = dictionary["artist"]
        self.title = dictionary["title"]
        self.difficulty = dictionary["difficulty"]
        self.level = dictionary["level"]
        self.released = dictionary["released"]

        if "_id" in dictionary:
            self.id = str(dictionary["_id"])

    def to_dict(self):
        return self.__dict__
