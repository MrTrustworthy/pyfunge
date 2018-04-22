import sys

from pyfunge import Grid
from pyfunge.executor import Executor


def run_on_file(filename):
    with open(filename) as infile:
        app = infile.read()
    grid = Grid.from_app_string(app)
    Executor().run(grid)


if __name__ == "__main__":
    run_on_file(sys.argv[1])
