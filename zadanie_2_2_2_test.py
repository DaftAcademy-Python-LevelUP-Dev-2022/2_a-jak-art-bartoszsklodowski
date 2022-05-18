import unittest

from file import sums_of_str_elements_are_equal


class CodingRoomsUnitTests(unittest.TestCase):
    @sums_of_str_elements_are_equal
    def two_simple_ints_first_is_negative(self):
        return "-4234 4324"

    @sums_of_str_elements_are_equal
    def two_simple_ints_both_are_negative(self):
        return "-123 -3111"

    def test_two_simple_ints_first_is_negative_are_not_equal(self):
        assert self.two_simple_ints_first_is_negative() == "-13 != 13"

    def test_two_simple_ints_first_is_negative_are_equal(self):
        assert self.two_simple_ints_both_are_negative() == "-6 == -6"


if __name__ == "__main__":
    unittest.main()
