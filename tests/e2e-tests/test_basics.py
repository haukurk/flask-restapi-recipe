import unittest
import os

os.environ['CONFIG'] = 'Development'

from restapi import app, version


class LoadingTestCase(unittest.TestCase):

    def test_is_main_routing_working(self):

        with app.test_client() as client:

            res = client.get('/')

            self.assertEqual(200, res.status_code)

    def test_weather_in_reykjavik(self):

        with app.test_client() as client:

            res = client.get('/api/v1/weather/ICXX0002')

            self.assertEqual(200, res.status_code)


if __name__ == '__main__':
    unittest.main()