import unittest

from file import greeter


class CodingRoomsUnitTests(unittest.TestCase):
    @greeter
    def name_surname(self):
        return "janek KOS"

    def test_result(self):
        self.assertEqual(self.name_surname(), "Aloha Janek Kos")


if __name__ == "__main__":
    unittest.main()
