
from pyfunge import Grid, Executor
from .apps import helloworld_app

def test_executor():
    grid = Grid.from_app_string(helloworld_app)
    try:
        Executor().run(grid)
    except SystemExit:
        return
    assert False, "This should call sys.exit()"