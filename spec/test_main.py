import unittest
from webtest import TestApp
import sys
sys.path.append('.')
import main

class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = TestApp(main.app)

    def tearDown(self):
        self.app.reset()

    def test_redirect(self):
        resp = self.app.get('/a')
        self.assertEqual(resp.status, '302 Found')

    def test_parse_url(self):
        resp = self.app.get('/a/bb/C__/d')
        self.assertTrue(resp.headers['Location'].startswith('https://twitter.com/intent/tweet?text=%40a%20%40bb%20%40C'))

    def test_parse_url_with_plus(self):
        resp = self.app.get('/a+bb+C__+d')
        self.assertTrue(resp.headers['Location'].startswith('https://twitter.com/intent/tweet?text=%40a%20%40bb%20%40C'))

if __name__ == '__main__':
    unittest.main()
