import unittest
from hello_world import *

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        """
        Set up the flask environment for testing
        """
        self.sample_message = greet()
        self.generated_html = generate_html(self.sample_message)

    def test_greet(self):
        """
        Test the greet function
        """
        self.assertIsInstance(greet(), str)
        self.assertEqual(greet(), 'Welcome to CI/CD 101 using GitHub Actions!')

    def test_generate_html(self):
        """
        Test the generate_html function
        """
        self.assertIsInstance(generate_html(self.sample_message), str)
        self.assertEqual(generate_html(self.sample_message), self.generated_html)

    def test_flask_app(self):
        """
        Test the flask app
        """
        self.assertIsInstance(app, Flask)
    
if __name__ == '__main__':
    unittest.main()
