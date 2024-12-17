class Cell:
    def __init__(self, column, row) -> None:
        self.col = column
        self.row = row 
        self.neighbours = []
    def __str__(self) -> str:
        return f"column: {self.col}, row: {self.row}" 