import random
import sys

from cell import Agent
from game import Game


ROWS = 10
COLS = 10


def main():
    seed = random.randrange(sys.maxsize)
    random.seed(seed)
    print("seed:", seed)

    agent = Agent(random.randint(0, ROWS-1), random.randint(0, COLS-1))

    g = Game(ROWS, COLS, agent)
    g.show_grid()

    g.fill_base_cost()
    g.show_cost()

    move = g.get_next_agent_move()
    print("Move:", move)


if __name__ == "__main__":
    main()
