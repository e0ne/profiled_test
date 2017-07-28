import unittest

from profiled_test import ProfiledTest


class SampleTest(ProfiledTest, unittest.TestCase): #, ProfiledTest):
    def test_sample(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
