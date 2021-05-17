import unittest

from tests.helpers import MockXYCell
from dehelpers.filters import like_year

class TestYearFunction(unittest.TestCase):
    
    # Test that filter returns what was expected
    def test_like_year_true(self): 
        
        # Create some test data
        mocked_year_cells = [
            MockXYCell(value=1997.0, x=5, y=1),
            MockXYCell(value=1998, x=6, y=1),
            MockXYCell(value='1999', x=7, y=1),
            MockXYCell(value=2000.0, x=8, y=1),
            MockXYCell(value=2001, x=9, y=1),
            MockXYCell(value='2002', x=10, y=1),
            MockXYCell(value=2010.0, x=11, y=1),
            MockXYCell(value=2011, x=12, y=1),
            MockXYCell(value='2012', x=13, y=1),
            MockXYCell(value=2019.0, x=14, y=1),
            MockXYCell(value=2020, x=15, y=1),
            MockXYCell(value='2021', x=15, y=1)
        ]
        
        for mock_cell in mocked_year_cells:
            self.assertEqual(like_year(mock_cell), True)
            
    # Test that filter returns False when expected to
    def test_like_year_false(self):

        mocked_non_year_cells = [
            MockXYCell(value='Dec', x=1, y=1),
            MockXYCell(value=20140, x=1, y=2),
            MockXYCell(value="2019Q1", x=1, y=3),
            MockXYCell(value=2100, x=1, y=4),
            MockXYCell(value='20111', x=1, y=5),
            MockXYCell(value='1900.0', x=1, y=6),
            MockXYCell(value='2025', x=1, y=7),
            MockXYCell(value='19921', x=1, y=6),
            MockXYCell(value='2019Feb', x=1, y=7),
            MockXYCell(value=202.0, x=1, y=8)   
        ]

        for mock_cell in mocked_non_year_cells:
            self.assertEqual(like_year(mock_cell), False)


if __name__ == '__main__':
    unittest.main()
