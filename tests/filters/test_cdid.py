# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.10.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import unittest

from tests.helpers import MockXYCell
from dehelpers.filters import cdid_filter

class TestCDIDfilter(unittest.TestCase):

    # Test that our filter returns what was expected
    def test_cdid_cells_return_true(self):

        # Create some test data
        mocked_cdid_cells = [
            MockXYCell(value="MK2N", x=1, y=2),
            MockXYCell(value="ABCD", x=1, y=3),
            MockXYCell(value="XT3H", x=1, y=4),
            MockXYCell(value="NIHN", x=1, y=5)
        ]
        for mock_cell in mocked_cdid_cells:
            self.assertEqual(cdid_filter(mock_cell), True)
            
    # Test that our filter returns False when expected to
    def test_NonCDID_cells_return_false(self):

        mocked_non_cdid_cells = [
            MockXYCell(value="2014", x=3, y=2),
            MockXYCell(value="London", x=3, y=3),
            MockXYCell(value="mcuh", x=3, y=4),
            MockXYCell(value="Exports", x=3, y=5),
        ]

        for mock_cell in mocked_non_cdid_cells:
            self.assertEqual(cdid_filter(mock_cell), False)

if __name__ == '__main__':
    unittest.main()
