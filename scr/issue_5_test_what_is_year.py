import unittest

from scr.what_is_year_now import what_is_year_now
from unittest.mock import MagicMock, patch


class TestWhatIsYear(unittest.TestCase):

    def test_get_data(self):
        what_is_year_now.resp_json = MagicMock()
        what_is_year_now.resp_json('{"$id":"1",'
                                   '"currentDateTime":"2020-04-20T13:53Z",'
                                   '"utcOffset":"00:00:00",'
                                   '"isDayLightSavingsTime":false,"dayOfTheWeek":"Monday",'
                                   '"timeZoneName":"UTC","currentFileTime":132318644194100285,'
                                   '"ordinalDate":"2020-111","serviceResponse":null}'
                                   )
        what_is_year_now.resp_json.assert_called_with('{"$id":"1",'
                                                      '"currentDateTime":"2020-04-20T13:53Z",'
                                                      '"utcOffset":"00:00:00",'
                                                      '"isDayLightSavingsTime":false,'
                                                      '"dayOfTheWeek":"Monday","timeZoneName":"UTC",'
                                                      '"currentFileTime":132318644194100285,'
                                                      '"ordinalDate":"2020-111","serviceResponse":null}'

                                                      )


if __name__ == '__main__':
    unittest.main()
