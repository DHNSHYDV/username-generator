import unittest
import re
from username_generator import UsernameGenerator


class TestUsernameGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = UsernameGenerator()

    def test_generate_random(self):
        # Test default length
        username = self.generator.generate_random()
        self.assertEqual(len(username), 8)
        
        # Test custom length
        custom_length = 12
        username = self.generator.generate_random(custom_length)
        self.assertEqual(len(username), custom_length)
        
        # Test character set (should only contain letters and digits)
        pattern = r'^[a-zA-Z0-9]+$'
        self.assertTrue(re.match(pattern, username))

    def test_generate_adjective_noun(self):
        # Test with number
        username = self.generator.generate_adjective_noun(with_number=True)
        pattern = r'^[A-Z][a-z]+[A-Z][a-z]+\d+$'
        self.assertTrue(re.match(pattern, username))
        
        # Test without number
        username = self.generator.generate_adjective_noun(with_number=False)
        pattern = r'^[A-Z][a-z]+[A-Z][a-z]+$'
        self.assertTrue(re.match(pattern, username))

    def test_generate_themed(self):
        # Test with valid themes
        for theme in ["nature", "tech", "fantasy"]:
            username = self.generator.generate_themed(theme)
            self.assertTrue(len(username) > 0)
        
        # Test invalid theme
        with self.assertRaises(ValueError):
            self.generator.generate_themed("invalid_theme")

    def test_generate_from_name(self):
        # Test with a simple name
        username = self.generator.generate_from_name("John", with_number=True)
        self.assertTrue(username.startswith("john"))
        
        # Test with a complex name (with spaces)
        username = self.generator.generate_from_name("John Doe", with_number=False)
        self.assertTrue(username.startswith("johndoe"))

    def test_generate_multiple(self):
        # Test default count
        usernames = self.generator.generate_multiple()
        self.assertEqual(len(usernames), 5)
        
        # Test custom count
        custom_count = 10
        usernames = self.generator.generate_multiple(count=custom_count)
        self.assertEqual(len(usernames), custom_count)
        
        # Test invalid method
        with self.assertRaises(ValueError):
            self.generator.generate_multiple(method="invalid_method")


if __name__ == '__main__':
    unittest.main()