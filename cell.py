class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.cost = -1


class Empty(Cell):
    def __init__(self, row, col):
        super().__init__(row, col)

    def __repr__(self):
        return "."


class Brick(Cell):
    def __init__(self, row, col, health=2):
        super().__init__(row, col)
        self.health = health

    def __repr__(self):
        return "#"


class Steel(Cell):
    def __init__(self, row, col):
        super().__init__(row, col)

    def __repr__(self):
        return "#"


class Base(Cell):
    def __init__(self, row, col, health=1):
        super().__init__(row, col)
        self.health = health
        self.cost = 0

    def __repr__(self):
        return "C"


class Agent(Cell):
    def __init__(self, row, col):
        super().__init__(row, col)

    def __repr__(self):
        return "A"
