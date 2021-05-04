
import unittest

# from tests.helpers import MockXYCell
from dehelpers.filters import like_observations

from databaker.framework import *

class TestObservationsFunction(unittest.TestCase):
    
    # Test that our filter returns what was expected
    def test_like_observations_success(self):
        
        tabs = loadxlstabs("tests/filters/sources/OIC.xls") # load tabs
        tab = tabs[2] # Table 1a
        
        actual_observation = like_observations(tab)
        expected_observation = tab.excel_ref('C11').expand(DOWN).expand(RIGHT).is_not_blank()
    
        self.assertEqual(actual_observation, expected_observation)
        
        
    def test_like_observations_failure(self):
        
        
        tabs = loadxlstabs("tests/filters/sources/OIC.xls") 
        tab = tabs[2] #Table 1a

        actual_observation = like_observations(tab)
        expected_observation = tab.excel_ref("A11").expand(DOWN).is_not_blank() |tab.excel_ref('C11').expand(DOWN).expand(RIGHT).is_not_blank() # year dimension added to observations
        self.assertEqual(actual_observation, expected_observation)

    def test_like_observations_exception(self):
        tabs = loadxlstabs("tests/filters/sources/OIC.xls") 
        tab = tabs[1] # Contents
        
        with self.assertRaises(TypeError) as exception_context:
            like_observations(tab)
        self.assertEqual(
            str(exception_context.exception),
            "Observation data from source data must be of type <float> or <int>"
        )
    
        
if __name__ == '__main__':
    unittest.main()
