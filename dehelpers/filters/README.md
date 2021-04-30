
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


## Filter Classes (also known as filters that take arguments)

So a filter is just a function that _calls_ some behaviour when you pass it a variable (because function have a method named `__call__`).

But - functions are not the only things that can be __call__'ed , so can classes _if_ you give them a `__call__` method.

### But...why would you use a class fo make a filter?

Python classes have a very important concept called `self`. The `self` of a class is literally what it sounds like, it's a means for a class to reference itself, or ask itself "what do I know?" or "can I do this thing?".

Consider this example:

```python
class PetClass:

    # When you __init__ you dictate what happens when the class is instantiated/created
    # in this case we're "remembering" the pet value as self.pet
    def __init__(self, pet):
        self.pet = pet

    # Call is how you define behaviour for when you pass variables (or call on) your class AFTER it's been instantiated.
    def __call__(self, name):
        # Note - I'm using self.pet here, because our class "remembers" this property
        print(f'My name is {name} and I like my {self.pet}')

```

So this class would behave like the following:

```
snake_likers = PetClass("Python")

snake_likers("Monty")
>> "My name is Monty and I like my Python"

snake_likers("Brian")
>> "My name is Brian and I like my Python"

cat_likers = PetClass("Cat")
cat_likers("Pat")
>> "My name is Pat and I like my Cat
```

### Putting It Together

Consider the following.

_Note - the important thing here is to understand the sequence (a) `__init__` is called when you instantied the class with the initial arguments - then - (b) the xycells are passed into that instanitated thing one at a time via `__call__`._

```python
class is_one_of:
   """A filter that will return true if the cell value is one of a defined list of values"""

    def __init__(self, our_chosen_values):
        self.our_chosen_values = our_chosen_values

    def __call__(self, xy_cell):
        if xy_cell.value in self.our_chosen_values:
            return True
        return False
```

And to use it

```python
# Filer to only inlcude calls whose value is foo, bar or baz
tab.filter(is_one_of(["foo", "bar", "baz"]))
```

To finish, this is a more thorough example you can run in any python interpreter

```python
class is_one_of:
    """A filter that will return true if the cell value is one of a defined list of values"""

    def __init__(self, our_chosen_values):
        self.our_chosen_values = our_chosen_values

    def __call__(self, xy_cell):
        if xy_cell.value in self.our_chosen_values:
            return True
        return False
    
# Note: again we're defining a simple class, just so we can "mock" a primitive xycell for this example
# i.e our filter looks for .value, FakeCell has a .value, therefore it'll work
class FakeCell:
    
    def __init__(self, value):
        self.value = value
        
fake_cells = [FakeCell(1), FakeCell(2), FakeCell(3), FakeCell(4)]

# Show that our instanitated "filter" return True or False when __call__'d
this_filter = is_one_of([1,2])
for fake_cell in fake_cells:
    print(f'Cell with value: {fake_cell.value} has value 1 or 2: {this_filter(fake_cell)}')
```

Running this code will result in:

```
>> Cell with value: 1 has value 1 or 2: True
>> Cell with value: 2 has value 1 or 2: True
>> Cell with value: 3 has value 1 or 2: False
>> Cell with value: 4 has value 1 or 2: False
```