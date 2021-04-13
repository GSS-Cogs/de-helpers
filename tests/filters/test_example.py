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