# De Helpers

A helper library of simple data transformation helpers, for use by the idp dissemination data engineering team.

## Installing

`pip install --update --no-cache git+git://github.com/GSS-Cogs/de-helpers.git`

## Usage

To use a custom filter for databaker, you can import them (to use the example) via:

```
from dehelpers.filters import foofilter 
```

## A note on tests

We need to have them for everything, regardless of how trivial. Given that these are software functions that will run in many potential pipelines.

BDD doesn't necessarily make sense with lots of small unconnected helper functions (if you function isn't small, it doesn't belong here), so for now I've put in a basic unit test setup. You can run the tests via:

```
python -m unittest discover -v tests
```
