from pyfunge import Grid

from .apps import helloworld_app

def test_grid_parsing():
    grid = Grid.from_app_string(helloworld_app)
    assert grid.size_x == 16 and grid.size_y == 5
    print(grid.grid)