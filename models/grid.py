import random
import sys
sys.path.append("models")

from cell import Cell
from black import Black
from white import White
from grid_creator import GridCreator


class Grid:
    def __init__(self, grid_width, grid_height) -> None:
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.grid = self.create_grid()
        self.find_neighbours()

    def __str__(self) -> str:
        grid_str = ""
        for i in self.grid:
            grid_str += ", ".join([str(j.colour) for j in i]) + "\n"
        return grid_str

    def create_grid(self):
        return [[random.choice([Black(i, j), White(i, j)]) 
            for i in range(self.grid_width)] 
                for j in range(self.grid_height)]
    
    def iterate_neighbours(self, cell):
        for row_number, row_list in enumerate(self.grid):
            for col_number, col_cell in enumerate(row_list):
                if(abs(col_number - cell.col) <= 1 and abs(row_number - cell.row) <= 1):
                    if(col_number - cell.col == 0 and row_number - cell.row == 0):
                        continue
                    else:
                        cell.neighbours.append(col_cell)
    
    def find_neighbours(self):
        for i in self.grid:
            for j in i:
                self.iterate_neighbours(j)

sample_grid = Grid(3, 3)
print(sample_grid)
print(*sample_grid.grid[2][2].neighbours)

