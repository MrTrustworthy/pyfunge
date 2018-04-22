import sys
from random import choice
from typing import Tuple, TYPE_CHECKING

from ..point import Point
from ..symbol import Symbol

if TYPE_CHECKING:
    from ..grid import Grid
    from ..stack import Stack


class DirectionRight(Symbol):
    symbol_names = [">"]

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        return stack, Point(1, 0)


class DirectionLeft(Symbol):
    symbol_names = ["<"]

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        return stack, Point(-1, 0)


class DirectionDown(Symbol):
    symbol_names = ["v"]

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        return stack, Point(0, 1)


class DirectionUp(Symbol):
    symbol_names = ["^"]

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        return stack, Point(0, -1)


class DirectionRandom(Symbol):
    symbol_names = ["?"]

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        direction = choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        return stack, Point(*direction)


class Skip(Symbol):
    symbol_names = ["#"]

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        stack.skip_mode = True
        return stack, None


class CondRight(Symbol):
    symbol_names = ["_"]

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        x_dir = 1 if stack.pop() == 0 else -1
        return stack, Point(x_dir, 0)


class CondDown(Symbol):
    symbol_names = ["|"]

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        x_dir = 1 if stack.pop() == 0 else -1
        return stack, Point(0, x_dir)


class End(Symbol):
    symbol_names = ["@"]

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        print("Application has finished")
        sys.exit()
