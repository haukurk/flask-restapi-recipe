import sys
sys.path.append("../")

import unittest
import os

os.environ['RESTAPICONFIG'] = 'UnitTesting'  # Use UnitTesting environment.

from restapi import app, db
from restapi.modules import statuscodes


class LoadingTestCase(unittest.TestCase):
    """
    Example Test Cases for our precious RESTful API.
    """

    def setUp(self):
        """
        Start by creating a fresh DB.
        Note we should be using a TEST/UNITTEST environment defined with: os.environ['RESTAPICONFIG'].
        """
        db.create_all()

    def tearDown(self):
        """
        Close all sessions and drop all database object in the current environment.
        """
        db.session.remove()
        db.drop_all()

    def test_is_main_routing_working(self):
        """
        Test if the main route is answering with the correct status code.
        """
        with app.test_client() as client:
            res = client.get('/')

            self.assertEqual(200, res.status_code)

    def test_authorization_add_cake(self):
        """
        Test if you are indeed not able to create a cake when not specifying an API key.
        """
        with app.test_client() as client:
            res = client.post('/api/v1.1/cakes/', data=dict(
                cakename="test name",
                bakername="test baker",
                price="1"
            ), follow_redirects=True, environ_base={
                'HTTP_USER_AGENT': 'Chrome',
                'REMOTE_ADDR': '127.0.0.1'
            })

            self.assertEqual(statuscodes.HTTP_UNAUTHORIZED, res.status_code)

    def test_public_list_cakes(self):
        """
        Test if you are able to get all cake object, which need no authorization and if it return the correct status code.
        """
        with app.test_client() as client:
            res = client.get('/api/v1.1/cakes/', follow_redirects=True, environ_base={
                'HTTP_USER_AGENT': 'Chrome',
                'REMOTE_ADDR': '127.0.0.1'
            })

            self.assertEqual(statuscodes.HTTP_OK, res.status_code)


if __name__ == '__main__':
    __package__ = "unittest_basics"
    __main__ = "unittest_basics"
    unittest.main()