import unittest

from tests.helpers import MockXYCell
from dehelpers.filters import like_cdid

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
            self.assertEqual(like_cdid(mock_cell), True)
            
    # Test that our filter returns False when expected to
    def test_non_cdid_cells_return_false(self):

        mocked_non_cdid_cells = [
            MockXYCell(value='2014Q2', x=3, y=2),
            MockXYCell(value="Lo8n", x=3, y=3),
            MockXYCell(value="mcuh", x=3, y=4),
            MockXYCell(value="Exports", x=3, y=5),
            MockXYCell(value=True, x=3, y=6),
            MockXYCell(value=19.6, x=3, y=7),
            MockXYCell(value="", x=2, y=6),
            MockXYCell(value=2019, x=2, y=7),
            MockXYCell(value=None, x=2, y=8),
            MockXYCell(value=2021-0o4-23, x=4, y=1)
        ]

        for mock_cell in mocked_non_cdid_cells:
            self.assertEqual(like_cdid(mock_cell), False)

if __name__ == '__main__':
    unittest.main()
