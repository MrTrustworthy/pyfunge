from ..symbol import Symbol

from typing import Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from ..grid import Grid, Point
    from ..stack import Stack


class Empty(Symbol):
    symbol_names = [" ", "__default__"]

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        return stack, None
