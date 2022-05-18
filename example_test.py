import unittest

from file import greeter


class CodingRoomsUnitTests(unittest.TestCase):
    @greeter
    def name_surname(self):
        return "anna kowalska"

    def test_result(self):
        self.assertEqual(self.name_surname(), "Aloha Anna Kowalska")


if __name__ == "__main__":
    unittest.main()
