import unittest

from tests.helpers import MockXYCell
from dehelpers.filters import like_float

class TestFloatFunction(unittest.TestCase):
    
    # Test that filter returns what was expected
    def test_like_float_true(self): 
        
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
            self.assertEqual(like_float(mock_cell), True)
            
    # Test that filter returns False when expected to
    def test_like_float_false(self):

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
            self.assertEqual(like_float(mock_cell), False)
            
     
if __name__ == '__main__':
    unittest.main()
