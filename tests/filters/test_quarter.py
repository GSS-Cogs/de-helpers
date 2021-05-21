import unittest

from tests.helpers import MockXYCell
from dehelpers.filters import like_quarter

class TestQuarterFunction(unittest.TestCase):
    
    # Test that filter returns what was expected
    def test_like_quarter_true(self): 
        
        # Create some test data
        mocked_quarter_cells = [
            MockXYCell(value='Q1', x=5, y=1),
            MockXYCell(value='Q2', x=6, y=1),
            MockXYCell(value='Q3', x=7, y=1),
            MockXYCell(value='Q4', x=8, y=1),
        ]
        
        for mock_cell in mocked_quarter_cells:
            self.assertEqual(like_quarter(mock_cell), True)
            
    # Test that filter returns False when expected to
    def test_like_quarter_false(self):

        mocked_non_quarter_cells = [
            MockXYCell(value='Q5', x=1, y=1),
            MockXYCell(value='QQ2', x=1, y=2),
            MockXYCell(value="2019Q1", x=1, y=3),
            MockXYCell(value='2100Q', x=1, y=4),
            MockXYCell(value=20, x=1, y=5),
            MockXYCell(value='1Q', x=1, y=6),
            MockXYCell(value='Q1Q2', x=1, y=7),
            MockXYCell(value='2Q1', x=1, y=6),
            MockXYCell(value='2019Feb', x=1, y=7),
            MockXYCell(value='Q', x=1, y=8)   
        ]

        for mock_cell in mocked_non_quarter_cells:
            self.assertEqual(like_quarter(mock_cell), False)


if __name__ == '__main__':
    unittest.main()
