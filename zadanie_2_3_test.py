import unittest

from file import format_output


class CodingRoomsUnitTests(unittest.TestCase):
    @format_output("first_name__last_name", "city")
    def first_func(self):
        return {
            "first_name": "Jan",
            "last_name": "Kowalski",
            "city": "Warsaw",
        }

    @format_output("company_name", "address", "city_code__city__country")
    def second_func(self):
        return {
            "country": "Poland",
            "company_name": "DaftCode",
            "address": "Pl. Europejski 1",
            "city": "Warsaw",
            "city_code": "00-844",
        }

    @format_output("age")
    def third_func(self):
        return {"first_name": "Jan", "last_name": "Kowalski"}

    @format_output("first_name__last_name", "first_name__age")
    def fourth_func(self):
        return {"first_name": "Jan", "last_name": "Kowalski"}

    @format_output("first_name")
    def fifth_func(self):
        return {"first_name": "Jan", "last_name": "Kowalski"}

    @format_output("first_name", "mobile")
    def sixth_func(self):
        return {"first_name": "Jan", "last_name": "Kowalski", "mobile": ""}

    def test_first_func(self):
        self.assertEqual(
            self.first_func(),
            {"first_name__last_name": "Jan Kowalski", "city": "Warsaw"},
        )

    def test_second_func(self):
        self.assertEqual(
            self.second_func(),
            {
                "company_name": "DaftCode",
                "address": "Pl. Europejski 1",
                "city_code__city__country": "00-844 Warsaw Poland",
            },
        )

    def test_third_func(self):
        with self.assertRaises(ValueError):
            self.third_func()

    def test_fourth_func(self):
        with self.assertRaises(ValueError):
            self.fourth_func()

    def test_fifth_func(self):
        self.assertEqual(
            self.fifth_func(),
            {
                "first_name": "Jan",
            },
        )

    def test_sixth_func(self):
        self.assertEqual(
            self.sixth_func(),
            {
                "first_name": "Jan",
                "mobile": "Empty value",
            },
        )


if __name__ == "__main__":
    unittest.main()
