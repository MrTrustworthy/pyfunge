from ..symbol import Symbol
from ..point import Point
from typing import Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from ..grid import Grid
    from ..stack import Stack


class Duplicate(Symbol):
    symbol_names = [":"]

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        val = stack.pop()
        stack.push(val)
        stack.push(val)
        return stack, None


class Swap(Symbol):
    symbol_names = ["\\"]

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        last, before = stack.pop(), stack.pop()
        stack.push(last)
        stack.push(before)
        return stack, None


class Discard(Symbol):
    symbol_names = ["$"]

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        stack.pop()
        return stack, None


class PrintInt(Symbol):
    symbol_names = ["."]

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        print(stack.pop(), end=" ")
        return stack, None


class PrintString(Symbol):
    symbol_names = [","]

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        print(chr(stack.pop()), end="")
        return stack, None
