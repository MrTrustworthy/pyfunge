from .grid import Grid
from .point import Point
from .stack import Stack
from .symbols import *

class Executor:

    def run(self, grid: Grid):
        stack = Stack()
        grid = grid
        pointer = Point(0, 0)
        direction = Point(1, 0)
        while True:
            symbol = grid.get(pointer)
            stack, new_direction = symbol.execute_base(stack, grid)
            direction = new_direction if new_direction is not None else direction
            pointer = self.update_pointer(pointer, direction, grid)

    def update_pointer(self, base: Point, point: Point, grid: Grid):
        new_x = base.x + point.x
        if new_x < 0:
            new_x = grid.size_x - new_x
        elif new_x >= grid.size_x:
            new_x = new_x - grid.size_x

        new_y = base.y + point.y
        if new_y < 0:
            new_y = grid.size_y - new_y
        elif new_y >= grid.size_y:
            new_y = new_y - grid.size_y

        return Point(new_x, new_y)
