import unittest
from unittest.mock import patch, Mock

from songs.repositories import SongRepository
from songs.models import Song


class TestRatingRepositoryMethods(unittest.TestCase):

    @patch("songs.songs_collection.find")
    def test_get_songs(self, mock_find):
        song_dict = {
            "_id": 1,
            "artist": "Oliver Koletzki",
            "title": "No Man No Cry",
            "difficulty": 5,
            "level": 4,
            "released": "2014-01-01"
        }
        song = Song(song_dict)

        mock_find.return_value = Mock(
            skip=lambda x: Mock(
                limit=Mock(return_value=(song_dict, song_dict))
            )
        )

        songs = SongRepository.get_songs(0, 20)

        self.assertEqual(songs[0], song.__dict__)


if __name__ == '__main__':
    unittest.main()
