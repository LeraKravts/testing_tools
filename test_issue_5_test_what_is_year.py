import json
import unittest
import urllib.request


import test_what_is_year_now
from test_what_is_year_now import what_is_year_now
from unittest.mock import MagicMock


class TestWhatIsYear(unittest.TestCase):

    def test_get_data(self):
        json.load = MagicMock(return_value={"currentDateTime": "2020-04-20T13:53Z"})
        self.assertEqual(2020, what_is_year_now())

    def test_get_data_2(self):
        json.load = MagicMock(return_value={"currentDateTime": "20.04.2020T13:53Z"})
        self.assertEqual(2020, what_is_year_now())

    def test_type(self):
        json.load = MagicMock(return_value={"currentDateTime": 'T13:53Z'})
        self.assertRaises(ValueError, return_value={"currentDateTime": 'T13:53Z'})


if __name__ == '__main__':
    unittest.main()
