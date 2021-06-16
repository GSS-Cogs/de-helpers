import unittest

from tests.helpers import MockXYCell
from dehelpers.filters import like_ons_geography, is_numeric, like_cdid

class TestONSGeographyFilter(unittest.TestCase):
    
    # Test that filter returns what was expected
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
            MockXYCell(value='E920000G1', x=3, y=1),
            MockXYCell(value='s92000003', x=3, y=2),
            MockXYCell(value='x9200000y', x=3, y=3),
            MockXYCell(value='K120Ty001', x=3, y=4),
            MockXYCell(value='1200cab09', x=3, y=5),
            MockXYCell(value=200000016, x=3, y=6),
            MockXYCell(value='E100e0017', x=3, y=7),
            MockXYCell(value='S1200004s', x=3, y=8),
            MockXYCell(value='Nn9000002', x=3, y=9),
            MockXYCell(value='E0700020k', x=3, y=10),
            MockXYCell(value='N09N00ONS', x=3, y=11),
            MockXYCell(value='506n00n05', x=3, y=12),
            MockXYCell(value='0E8000035', x=3, y=13)
        ]
        
        for mock_cell in mocked_non_ons_geography_cells:
            self.assertEqual(like_ons_geography(mock_cell), False)
    
class TestIsNumericFunction(unittest.TestCase):
    
    # Test that filter returns what was expected
    def test_is_numeric_true(self): 
        
        # Create some test data
        mocked_float_cells = [
            MockXYCell(value=1997.0, x=1, y=1),
            MockXYCell(value=1998.0, x=2, y=1),
            MockXYCell(value=1999.0, x=3, y=1),
            MockXYCell(value=2000.0, x=4, y=1),
            MockXYCell(value=2001.0, x=5, y=1),
            MockXYCell(value=390.0, x=1, y=3),
            MockXYCell(value=2020.0, x=2, y=3),
            MockXYCell(value=1997.0, x=3, y=3),
            MockXYCell(value=1998.0, x=4, y=3),
            MockXYCell(value=230.0, x=5, y=3),
            MockXYCell(value=1.0, x=1, y=4),
            MockXYCell(value=2317.0, x=2, y=4),
            MockXYCell(value=13.0, x=3, y=4),
            MockXYCell(value=5.0, x=4, y=4),
            MockXYCell(value=1998.0, x=5, y=4),
            MockXYCell(value=2020.0, x=5, y=5)
        ]
        
        for mock_cell in mocked_float_cells:
            self.assertEqual(is_numeric(mock_cell), True)
            
    # Test that filter returns False when expected to
    def test_is_numeric_false(self):

        mocked_non_float_cells = [
            MockXYCell(value='2014Q2', x=3, y=2),
            MockXYCell(value="Lo8n", x=3, y=3),
            MockXYCell(value="mcuh", x=3, y=4),
            MockXYCell(value="Exports", x=3, y=5),
            MockXYCell(value='abcd', x=3, y=6),
            MockXYCell(value='ABCD', x=3, y=7),
            MockXYCell(value='', x=2, y=6),
            MockXYCell(value='2019Feb', x=2, y=7),
            MockXYCell(value='1a.', x=2, y=8),
            MockXYCell(value=None, x=4, y=1)
        ]

        for mock_cell in mocked_non_float_cells:
            self.assertEqual(is_numeric(mock_cell), False)
            

class TestCDIDfilter(unittest.TestCase):

    # Test that filter returns what was expected
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
            
    # Test that filter returns False when expected to
    def test_non_cdid_cells_return_false(self):

        mocked_non_cdid_cells = [
            MockXYCell(value='2014Q2', x=3, y=2),
            MockXYCell(value="Lo8n", x=3, y=3),
            MockXYCell(value="m3uh", x=3, y=4),
            MockXYCell(value="N1hn", x=3, y=5),
            MockXYCell(value=True, x=3, y=6),
            MockXYCell(value=19.6, x=3, y=7),
            MockXYCell(value="", x=2, y=6),
            MockXYCell(value=2019, x=2, y=7),
            MockXYCell(value=None, x=2, y=8),
            MockXYCell(value='MUC', x=4, y=1),
            MockXYCell(value='Mu3H', x=4, y=2)
        ]

        for mock_cell in mocked_non_cdid_cells:
            self.assertEqual(like_cdid(mock_cell), False)

if __name__ == '__main__':
    unittest.main()