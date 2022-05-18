import unittest

from file import greeter


class CodingRoomsUnitTests(unittest.TestCase):
    @greeter
    def name_surname(self):
        return "JAN sebastian baCH"

    def test_result(self):
        self.assertEqual(self.name_surname(), "Aloha Jan Sebastian Bach")


if __name__ == "__main__":
    unittest.main()
