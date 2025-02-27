import random
from cell import Agent, Brick, Center, Empty, Steel


class Game:
    def __init__(self, rows, cols, agent):
        self.rows = rows
        self.cols = cols
        self.grid = [[Empty(r, c) for c in range(cols)] for r in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if not random.choice(range(3)):  # roll dice
                    val = random.choice([Brick(r, c), Steel(r, c)])
                    self.grid[r][c] = val

        self.agent = agent
        self.grid[agent.row][agent.col] = self.agent

        while True:
            base_r = random.randint(0, rows-1)
            base_c = random.randint(0, cols-1)
            # try again if row and col match that of agent
            if not (base_r == agent.row and base_c == agent.col):
                break
        self.base = Center(base_r, base_c)
        self.grid[base_r][base_c] = self.base

    def fill_base_cost(self):
        # A*
        q = [(self.base.row, self.base.col)]
        while q:
            source_r, source_c = q.pop(0)
            cost_val = self.grid[source_r][source_c].cost + 1
            neighbors = list(self.neighborhood(source_r, source_c).values())
            neighbors.sort(key=lambda n: n.cost)
            for n in neighbors:
                if not (isinstance(n, Empty) or isinstance(n, Center) or isinstance(n, Agent)):
                    continue
                r, c = n.row, n.col
                if self.grid[r][c].cost != -1:
                    continue
                self.grid[r][c].cost = cost_val
                q.append((r, c))

    def get_next_agent_move(self):
        neighbors = self.neighborhood(self.agent.row, self.agent.col)
        empty_neighbors = {k: v for k, v in neighbors.items(
        ) if isinstance(v, Empty) or isinstance(v, Center)}
        if not empty_neighbors:
            print("No empty neighbors! :(")
            return "X"
        direction = min(empty_neighbors.keys(),
                        key=lambda k: empty_neighbors[k].cost)
        if empty_neighbors[direction].cost < 0:
            print("Agent is blocked! :(")
            return "X"
        return direction

    def neighborhood(self, row, col):
        n = {}

        directions = {"N": (-1, 0), "E": (0, -1), "W": (0, 1), "S": (1, 0)}
        for key, val in directions.items():
            dr, dc = val
            if not (0 <= row + dr < self.rows):
                continue
            if not (0 <= col + dc < self.cols):
                continue

            n[key] = self.grid[row + dr][col + dc]

        return n

    def __repr__(self):
        s = ""
        s += "+" + "-"*self.rows + "+\n"
        for row in self.grid:
            s += "|"
            for cell in row:
                s += str(cell)
            s += "|\n"
        s += "+" + "-"*self.rows + "+"
        return s

    def show_grid(self):
        print(self)

    def cost_string(self):
        s = ""
        s += "+" + "-"*self.rows + "+\n"
        for row in self.grid:
            s += "|"
            for cell in row:
                if cell.cost > 9:
                    s += "."
                elif cell.cost >= 0:
                    s += str(cell.cost)
                else:
                    s += "#"
            s += "|\n"
        s += "+" + "-"*self.rows + "+"
        return s

    def show_cost(self):
        print(self.cost_string())
