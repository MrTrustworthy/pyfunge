from abc import ABCMeta, abstractmethod
from typing import Type, Tuple, TYPE_CHECKING
from .stack import Stack
from collections import namedtuple


if TYPE_CHECKING:
    from .grid import Grid
    from .point import Point


class SymbolMeta(ABCMeta):
    _symbol_classes = {}

    def __new__(mcs, class_name, class_parents, class_attr):
        new_class = super().__new__(mcs, class_name, class_parents, class_attr)

        # Only register subclasses
        if class_name == "Symbol":
            return new_class

        # assert that 'symbol_names' are set
        symbol_names = class_attr.get("symbol_names")
        assert isinstance(symbol_names, list), "Subclass of Symbol needs to define a 'symbol_names' (list) attribute"

        # register all symbol names
        for symbol_name in symbol_names:
            assert SymbolMeta._symbol_classes.get(symbol_name) is None, \
                f"Class for {symbol_name} has already been registered"
            mcs._symbol_classes[symbol_name] = new_class

        return new_class


class Symbol(metaclass=SymbolMeta):

    def __init__(self, symbol_string: str):
        self.symbol_string = symbol_string

    def execute_base(self, stack: Stack, grid: "Grid") -> Tuple[Stack, "Point"]:
        if stack.skip_mode == True:
            stack.skip_mode = False
            return stack, None
        if stack.string_mode == True:
            if self.symbol_string == '"':
                stack.string_mode = False
            else:
                stack.push(ord(self.symbol_string))
            return stack, None

        try:
            stack, point = self.execute(stack, grid)
            assert stack is not None
            return stack, point
        except TypeError:
            raise AttributeError(f"execute() of {self} needs to return a stack and pointer/None!")

    @abstractmethod
    def execute(self, stack: Stack, grid: "Grid") -> Tuple[Stack, "Point"]:
        print("BLUB")

    @classmethod
    def instance_from_symbol_name(cls, symbol_string: str) -> "Symbol":
        _class = cls._symbol_classes.get(symbol_string, cls._symbol_classes.get("__default__"))
        if _class is None:
            raise AttributeError("No class registered for classname", symbol_string, "and no default available")
        return _class(symbol_string)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.symbol_string})"
