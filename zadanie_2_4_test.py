import unittest

from file import add_method_to_instance


class Dummy:
    pass


@add_method_to_instance(Dummy)
def foo():
    return "Hello world!"


class CodingRoomsUnitTests(unittest.TestCase):
    def test_instance_method(self):
        self.assertEqual(Dummy().foo(), foo())


if __name__ == "__main__":
    unittest.main()
