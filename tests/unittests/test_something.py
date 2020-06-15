import unittest


class TestExample(unittest.TestCase):
    def test_pass(self):
        self.assertEqual("foo", "FOO".lower())


if __name__ == "__main__":
    unittest.main()
