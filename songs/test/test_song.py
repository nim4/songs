import unittest

from songs.models import Song


class TestSongMethods(unittest.TestCase):

    def test_init(self):
        song_dict = {
            "_id": 1,
            "artist": "Oliver Koletzki",
            "title": "No Man No Cry",
            "difficulty": 5,
            "level": 4,
            "released": "2014-01-01",
            "x": "x"
        }

        song = Song(song_dict)

        self.assertEqual(song.id, str(song_dict["_id"]))
        self.assertEqual(song.artist, song_dict["artist"])
        self.assertEqual(song.title, song_dict["title"])
        self.assertEqual(song.difficulty, song_dict["difficulty"])
        self.assertEqual(song.level, song_dict["level"])
        self.assertEqual(song.released, song_dict["released"])

        # Test filtering irrelevant keys
        self.assertIsNone(song.__dict__.get("x"))


if __name__ == '__main__':
    unittest.main()
