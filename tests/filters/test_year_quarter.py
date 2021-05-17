import unittest

from tests.helpers import MockXYCell
from dehelpers.filters import like_year_quarter

class TestYearQuarterFunction(unittest.TestCase):
    
    # Test that filter returns what was expected
    def test_year_quarter_true(self): 
        
        # Create some test data
        mocked_year_quarter_cells = [
            MockXYCell(value='1997Q1', x=5, y=1),
            MockXYCell(value=1998, x=6, y=1),
            MockXYCell(value='1999', x=7, y=1),
            MockXYCell(value=2000.0, x=8, y=1),
            MockXYCell(value='2001 Q2', x=9, y=1),
            MockXYCell(value='2002Q3', x=10, y=1),
            MockXYCell(value='2010 Q4', x=11, y=1),
            MockXYCell(value=2011, x=12, y=1),
            MockXYCell(value='2012', x=13, y=1),
            MockXYCell(value=2019.0, x=14, y=1),
            MockXYCell(value=2020, x=15, y=1),
            MockXYCell(value='2021', x=15, y=1)
        ]
        
        for mock_cell in mocked_year_quarter_cells:
            self.assertEqual(like_year_quarter(mock_cell), True)
            
    # Test that filter returns False when expected to
    def test_year_quarter_false(self):

        mocked_non_year_quarter_cells = [
            MockXYCell(value='2025', x=1, y=1),
            MockXYCell(value='201Q', x=1, y=2),
            MockXYCell(value="2019Q5", x=1, y=3),
            MockXYCell(value=210.0, x=1, y=4),
            MockXYCell(value='Q20111', x=1, y=5),
            MockXYCell(value='1900.0', x=1, y=6),
            MockXYCell(value='2025Q2', x=1, y=7),
            MockXYCell(value='199 Q3', x=1, y=6),
            MockXYCell(value='202Q', x=1, y=7),
            MockXYCell(value=202, x=1, y=8)   
        ]

        for mock_cell in mocked_non_year_quarter_cells:
            self.assertEqual(like_year_quarter(mock_cell), False)


if __name__ == '__main__':
    unittest.main()
