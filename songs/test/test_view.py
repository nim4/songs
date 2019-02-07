import json
import unittest
from flask import Flask
from flask_testing import TestCase
from unittest.mock import patch

from songs.views import *


class TestViewMethods(TestCase):

    def create_app(self):
        app = Flask(__name__)
        return app

    @patch("songs.repositories.SongRepository.get_songs")
    def test_get_songs(self, mock_get_songs):
        mock_get_songs.return_value = []
        response = get_songs()
        j = json.loads(response.response[0])

        mock_get_songs.assert_called_once_with(0, 10)
        self.assert200(response)
        self.assertEqual(j["songs"], [])

    @patch("songs.repositories.SongRepository.get_difficulty_by_level")
    def test_get_with_difficulty_level(self, mock_get_difficulty_by_level):
        mock_get_difficulty_by_level.return_value = 4
        response = get_with_difficulty_level()
        j = json.loads(response.response[0])

        mock_get_difficulty_by_level.assert_called_once_with(0)
        self.assert200(response)
        self.assertEqual(j["avg_difficulty"], 4)

        mock_get_difficulty_by_level.return_value = None
        _, status = get_with_difficulty_level()
        self.assertEqual(status, 404)

    @patch("songs.repositories.SongRepository.search")
    def test_search_songs(self, mock_search):
        mock_search.return_value = []
        response = search_songs()
        j = json.loads(response.response[0])

        mock_search.assert_called_once_with("")
        self.assert200(response)
        self.assertEqual(j["songs"], [])

    @patch("songs.repositories.RatingRepository.create")
    @patch("flask.request.get_json")
    def test_add_rating(self, mock_get_json, mock_create):
        mock_create.return_value = "123"
        mock_get_json.return_value = {
            "rating": 2,
            "song_id": "123"
        }
        response, status = add_rating()
        j = json.loads(response.response[0])

        self.assertEqual(status, 201)
        self.assertEqual(j["rating_id"], "123")

    @patch("songs.repositories.RatingRepository.get_song_avg_rating")
    def test_get_rating(self, mock_get_song_avg_rating):
        mock_get_song_avg_rating.return_value = 2.5
        response = get_rating("123")
        j = json.loads(response.response[0])

        mock_get_song_avg_rating.assert_called_once_with("123")
        self.assert200(response)
        self.assertEqual(j["avg_rating"], 2.5)


if __name__ == '__main__':
    unittest.main()
