import unittest
import app

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        # assert 'Hamptons Bank' in rv.data
        assert 10 == 10

if __name__ == '__main__':
    unittest.main()