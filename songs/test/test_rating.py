import unittest

from songs.models import Rating


class TestRatingMethods(unittest.TestCase):

    def test_init(self):
        rating_dict = {
            "song_id": "123",
            "rating": 5,
            "x": "x"
        }

        rating = Rating(rating_dict)

        self.assertEqual(rating.song_id, rating_dict["song_id"])
        self.assertEqual(rating.rating, rating_dict["rating"])

        # Test filtering irrelevant keys
        self.assertIsNone(rating.__dict__.get("x"))

        # Test out of range ratings
        rating_dict["rating"] = -1
        self.assertRaises(ValueError, lambda: Rating(rating_dict))

        rating_dict["rating"] = 6
        self.assertRaises(ValueError, lambda: Rating(rating_dict))


if __name__ == '__main__':
    unittest.main()
