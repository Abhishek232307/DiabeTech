import unittest
from app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        result = self.app.get('/')
        # assert the response status code
        self.assertEqual(result.status_code, 200)

if __name__ == "__main__":
    unittest.main()
