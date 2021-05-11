import unittest

from tests.helpers import MockXYCell
from dehelpers.filters import like_ons_geography

class TestONSGeographyFilter(unittest.TestCase):
    
    # Test that our filter returns what was expected
    def test_like_ons_geography_true(self): 
        
        # Create some test data
        mocked_ons_geography_cells = [
            MockXYCell(value='E92000001', x=1, y=1),
            MockXYCell(value='S92000003', x=1, y=2),
            MockXYCell(value='W92000004', x=1, y=3),
            MockXYCell(value='E12000001', x=1, y=4),
            MockXYCell(value='E12000009', x=1, y=5),
            MockXYCell(value='E10000016', x=1, y=6),
            MockXYCell(value='E10000017', x=1, y=7),
            MockXYCell(value='S12000041', x=1, y=8),
            MockXYCell(value='N09000002', x=1, y=9),
            MockXYCell(value='E07000200', x=1, y=10),
            MockXYCell(value='N09000003', x=1, y=11),
            MockXYCell(value='W06000015', x=1, y=12),
            MockXYCell(value='E08000035', x=1, y=13),
        ]
        
        for mock_cell in mocked_ons_geography_cells:
            self.assertEqual(like_ons_geography(mock_cell), True)
            
    # Test that our filter returns False when expected to
    def test_like_ons_geography_false(self):

        mocked_non_ons_geography_cells = [
            MockXYCell(value='2014', x=3, y=2),
            MockXYCell(value="Lo8n", x=3, y=3),
            MockXYCell(value="mcuh", x=3, y=4),
            MockXYCell(value="Exports", x=3, y=5),
            MockXYCell(value='abcd', x=3, y=6),
            MockXYCell(value='ABCD', x=3, y=7),
            MockXYCell(value='', x=2, y=6),
            MockXYCell(value='2019.0', x=2, y=7),
            MockXYCell(value='Feb', x=2, y=8),
            MockXYCell(value=None, x=4, y=1)
        ]

        for mock_cell in mocked_non_ons_geography_cells:
            self.assertEqual(like_ons_geography(mock_cell), False)
    

if __name__ == '__main__':
    unittest.main()
