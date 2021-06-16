
# Unit Tests

Unit tests are simple python tests for testing the functionality of stand alone functions.

## Running Unit Tests

We're using the simple unittest module from the standard python library here, no imports necessary. Just clone this repo and run:

`python -m unittest discover -v tests`

From the root of this repo, any tests present (and setup as per the below) will get discovered and ran.

When you push to a branch the same tests will be ran via a github action (just click actions at the top of the github repo).

## Setting Up New Unit Tests

To create unit tests you create a `test_<name of module being tests>.py` in the corresponding directory of the test root (hard to explain in text - see below).

So for example, if you wanted to add some new filters in `filters.py`, you'd setup your file structure as follows:

```
/dehelpers
    /filters.py
```

Then when you added the tests, you'd have a structure of

```
/dehelpers
    /filters.py
/tests
    /test_filters.py
```

This is enough that your new tests will get automatically discovered and ran either locally or on github.

## What does a test_ file look like?

There's an example here, but I'll break it down a bit too: [https://github.com/GSS-Cogs/de-helpers/blob/master/tests/filters/test_example.py](https://github.com/GSS-Cogs/de-helpers/blob/master/tests/filters/test_example.py)


* So the `class` is pretty always going to be named after the thing being tested.
* The method (`def <whatever>(self):`) is us confirming(asserting) than it does the expected with the given test data (in this case returns True with all of those mocked xycells). 
* `foofilter` is my specious example filter (that always returns "True", so it's literally filtering nothing).

## A better example:

If you had a filter called `cheesefilter` that returns True if the cell.value starts with the word "Cheese" else False, then some example unit tests for it would be

```python
import unittest

from tests.helpers import MockXYCell
from dehelpers.filters import cheesefilter

class TestCheeseFilter(unittest.TestCase):

    # Test that our filter returns True when expected to
    def test_cells_beginning_cheese_return_true(self):

        # Create some test data
        mocked_cheese_cells = [
            MockXYCell(value="Cheese", x=1, y=2),
            MockXYCell(value="Cheese Slices", x=2, y=2),
        ]

        for mock_cell in mocked_cheese_cells:
            self.assertEqual(cheesefilter(mock_cell), True)

    # Test that our filter returns False when expected to
    def test_cells_not_beginning_cheese_return_false(self):

        mocked_non_cheese_cells = [
            MockXYCell(value="I really don't like cheese", x=3, y=2),
            MockXYCell(value="You don't like cheese? heretic!", x=4, y=2)
        ]

        for mock_cell in mocked_non_cheese_cells:
            self.assertEqual(cheesefilter(mock_cell), False)

if __name__ == '__main__':
    unittest.main()
```







