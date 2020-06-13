import unittest


class TestExample(unittest.TestCase):
    def test_pass(self):
        self.assertEqual('foo', 'foo')

    def test_fail(self):
        self.assertEqual('g', 'y')


if __name__ == '__main__':
    unittest.main()
