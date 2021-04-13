
from typing import NamedTuple

# We might need to populate actual xt_cells, but that's a bit more
# than we need to get into until we have to.
class MockXYCell(NamedTuple):
    value: str
    x: int
    y: int
