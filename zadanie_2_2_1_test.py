import unittest

from file import sums_of_str_elements_are_equal


class CodingRoomsUnitTests(unittest.TestCase):
    @sums_of_str_elements_are_equal
    def two_simple_ints(self):
        return "1234 4321"

    @sums_of_str_elements_are_equal
    def two_simple_different_ints(self):
        return "1235 4321"

    def test_two_simple_ints_are_equal(self):
        assert self.two_simple_ints() == "10 == 10"

    def test_two_simple_ints_are_not_equal(self):
        assert self.two_simple_different_ints() == "11 != 10"


if __name__ == "__main__":
    unittest.main()
