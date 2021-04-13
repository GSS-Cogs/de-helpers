# De Helpers

A helper library of simple data transformation helpers, for use by the idp dissemination data engineering team.

## Installing

`pip install --update --no-cache git+git://github.com/GSS-Cogs/de-helpers.git`

## Usage

To use (for example) a custom filter for databaker, you can import them via:

```
from dehelpers.filters import foofilter 
```

## A note on tests

We need to have them for everything, regardless of how trivial. Given that these are software functions that will run in many potential pipelines.

BDD doenst really make sense with lots of small unconnected helper functions (if you function isn't small, it doesn't belong here), so I've put in a basic unit test setup. You can run the tests via:

```
python -m unittest discover -v tests
```
