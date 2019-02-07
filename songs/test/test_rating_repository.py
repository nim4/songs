import unittest
from unittest.mock import patch, Mock

from songs.repositories import RatingRepository
from songs.models import Rating


class TestRatingRepositoryMethods(unittest.TestCase):

    @patch("songs.ratings_collection.insert_one")
    def test_create(self, mock_insert_one):
        rating_dict = {
            "song_id": "123",
            "rating": 5
        }
        rating = Rating(rating_dict)

        mock_insert_one.return_value = Mock(inserted_id=321)

        inserted_id = RatingRepository.create(rating)
        self.assertEqual(inserted_id, "321")

    @patch("songs.ratings_collection.aggregate")
    def test_get_song_avg_rating(self, mock_aggregate):
        mock_aggregate.return_value = [{"avg": 2.5}]

        inserted_id = RatingRepository.get_song_avg_rating("123")
        self.assertEqual(inserted_id, 2.5)


if __name__ == '__main__':
    unittest.main()
