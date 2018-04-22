from pyfunge import Symbol
from pyfunge.symbols import *


def test_symbol():
    class SymbolTest(Symbol):
        symbol_names = ["_*"]

        def execute(self):
            pass

    cls = Symbol.instance_from_symbol_name("_*")
    assert isinstance(cls, SymbolTest)


def test_imports():
    assert isinstance(Symbol.instance_from_symbol_name(">"), directions.DirectionRight)
    assert isinstance(Symbol.instance_from_symbol_name("ddssdifughsdfg"), empty.Empty)
