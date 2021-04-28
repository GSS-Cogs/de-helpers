
# Filter Helpers

Conventions and standards for writing reusable filters.


## What is a filter?

A filter is a function (or class, of anything else you can `__call__`) that returns True or False when given an `_XYCell` object (this: https://github.com/sensiblecodeio/xypath/blob/6e58da44e9f7070089594fe6541ef8ce1eb2a34a/xypath/xypath.py#L92).

## Filter Conventions

There're two fundamental types of filters:

- (a) Filter to a thing we _know_ is exactly the thing we're looking for.
- (b) Filter to a thing we _think_ is _probably_ the thing we're looking for.

To explain the difference, if you take something like a CDID, if your filtering a selection and a cell value is say "ABCD" its probably a CDID, but technically it could be say the initials of a spreadsheet author with a 4 barrel name (or some other 4 letter acronym) that could get picked up by coincidence.

But if you filtered to find values that can be floats but cannot be integers then it's exact, it **is** a float. 

There's purpose/value in both, but we use strict conventions to clearly identify to the DE which of these types a given filter is.

### For Scenario (a):

Use a prefix of `is_<filter>`. For example `is_float`, `is_length4`

### For Scenario (b):

Use of prefix of `like_<filter>`. For example `like_CDID`, `like_ONSGeography`