from typing import List, Tuple, TYPE_CHECKING

from .symbol import Symbol

if TYPE_CHECKING:
    from .point import Point

StrArr2D = List[List[str]]
Arr2D = List[List[Symbol]]


class Grid:

    def __init__(self):
        self.grid = None
        self.size_x, self.size_y = None, None

    def load_app(self, app):
        self.grid = self._load_map(app)
        self.size_x, self.size_y = self.get_sizes(self.grid)

    def get(self, point: "Point") -> Symbol:
        return self.grid[point.y][point.x]

    def set(self, point: "Point", value: Symbol):
        self.grid[point.y][point.x] = value

    def _load_map(self, string: str) -> Arr2D:
        base = []
        for line in string.split('\n'):
            base.append(list(map(Symbol.instance_from_symbol_name, line)))
        return base

    def get_sizes(self, arr2d: Arr2D) -> Tuple[int, int]:
        y = len(arr2d)
        x = max(len(row) for row in arr2d)
        return x, y

    @classmethod
    def from_app_string(cls, app: str) -> "Grid":
        g = Grid()
        g.load_app(app)
        return g
