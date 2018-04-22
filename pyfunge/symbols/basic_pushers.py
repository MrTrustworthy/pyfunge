from typing import Tuple, TYPE_CHECKING

from ..symbol import Symbol

if TYPE_CHECKING:
    from ..grid import Grid, Point
    from ..stack import Stack


class Number(Symbol):
    symbol_names = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        stack.push(int(self.symbol_string))
        return stack, None


# StringEnd is handled by the base symbol class... overlooked that case initially
class StringStart(Symbol):
    symbol_names = ['"']

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        stack.string_mode = not stack.string_mode
        return stack, None


class Add(Symbol):
    symbol_names = ['+']

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        stack.push(stack.pop() + stack.pop())
        return stack, None


class Sub(Symbol):
    symbol_names = ['-']

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        a, b = stack.pop(), stack.pop()
        stack.push(b - a)
        return stack, None


class Mul(Symbol):
    symbol_names = ['*']

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        stack.push(stack.pop() * stack.pop())
        return stack, None


class Div(Symbol):
    symbol_names = ['/']

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        a, b = stack.pop(), stack.pop()
        stack.push(int(b / a))
        return stack, None


class Modulo(Symbol):
    symbol_names = ['%']

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        a, b = stack.pop(), stack.pop()
        stack.push(int(b % a))
        return stack, None


class Not(Symbol):
    symbol_names = ['!']

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        stack.push(int(not bool(stack.pop())))
        return stack, None


class Greater(Symbol):
    symbol_names = ['`']

    def execute(self, stack: "Stack", grid: "Grid") -> Tuple["Stack", "Point"]:
        a, b = stack.pop(), stack.pop()
        stack.push(int(b > a))
        return stack, None
