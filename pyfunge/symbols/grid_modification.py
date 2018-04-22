from ..symbol import Symbol
from ..point import Point
from typing import Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from ..grid import Grid
    from ..stack import Stack


class Put(Symbol):
    symbol_names = ["p"]

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        x, y, v = stack.pop(), stack.pop(), stack.pop()
        new_symbol = Symbol.instance_from_symbol_name(chr(v))
        grid.set(Point(x, y), new_symbol)
        return stack, None


class Get(Symbol):
    symbol_names = ["g"]

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        x, y = stack.pop(), stack.pop()
        stack.push(grid.get(Point(x, y)))
        return stack, None


class InputNumber(Symbol):
    symbol_names = ["&"]

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        number = int(input("Enter number:"))
        stack.push(number)
        return stack, None


class InputChar(Symbol):
    symbol_names = ["~"]

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        char = ord(input("Enter character:"))
        stack.push(char)
        return stack, None
