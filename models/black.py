import sys
sys.path.append("models")

from cell import Cell


class Black(Cell):
    colour = "0"
    def __init__(self, column, row) -> None:
        super().__init__(column, row) 
    def __str__(self) -> str:
        return "Colour: black, " + super().__str__()