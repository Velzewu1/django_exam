import sys
sys.path.append("models")

from cell import Cell


class White(Cell):
    colour = "1"
    def __init__(self, column, row) -> None:
        super().__init__(column, row) 
    def __str__(self) -> str:
        return "Colour: white, " + super().__str__()