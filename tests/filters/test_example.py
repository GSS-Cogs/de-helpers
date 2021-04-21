import unittest

from tests.helpers import MockXYCell
from dehelpers.filters import foofilter

class TestFooFilter(unittest.TestCase):

    # Test that our filter returns what was expected
    def test_all_cells_return_true(self):

        # Create some test data
        mocked_cells = [
            MockXYCell(value="Ray", x=1, y=2),
            MockXYCell(value="Egon", x=2, y=2),
            MockXYCell(value="Peter", x=3, y=2),
            MockXYCell(value="Winston", x=4, y=2)
        ]
        for mock_cell in mocked_cells:
            self.assertEqual(foofilter(mock_cell), True)

if __name__ == '__main__':
    unittest.main()


import unittest

from tests.helpers import MockXYCell
from dehelpers.filters import cheesefilter

class TestCheeseFilter(unittest.TestCase):

    # Test that our filter returns True when expected to
    def test_cells_beginning_cheese_return_true(self):

        # Create some test data
        mocked_cheese_cells = [
            MockXYCell(value="Cheese", x=1, y=2),
            MockXYCell(value="Cheese Slices", x=2, y=2),
        ]

        for mock_cell in mocked_cheese_cells:
            self.assertEqual(foofilter(mock_cell), True)

    # Test that our filter returns False when expected to
    def test_cells_not_beginning_cheese_return_false(self):

        mocked_non_cheese_cells = [
            MockXYCell(value="I really don't like cheese", x=3, y=2),
            MockXYCell(value="You don't like cheese? heretic!", x=4, y=2)
        ]

        for mock_cell in mocked_non_cheese_cells:
            self.assertEqual(foofilter(mock_cell), False)

if __name__ == '__main__':
    unittest.main()