import json
import unittest

from test_what_is_year_now import what_is_year_now
from unittest.mock import MagicMock


class TestWhatIsYear(unittest.TestCase):

    def test_get_data(self):
        json.load = MagicMock(return_value={"currentDateTime": "2020-04-20T13:53Z"})
        self.assertEqual(2020, what_is_year_now())

    def test_get_data_2(self):
        json.load = MagicMock(return_value={"currentDateTime": "20.04.2020T13:53Z"})
        self.assertEqual(2020, what_is_year_now())

    def test_get_data(self):
        json.load = MagicMock(return_value={"currentDateTime": "2025 04-20T13:53Z"})
        self.assertRaises(ValueError, what_is_year_now)


if __name__ == '__main__':
    unittest.main()
