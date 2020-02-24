import math
from Rules import apply_elementary_rule


class CellularAutomation:
    def __init__(self):
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.rule = apply_elementary_rule(110)
        print(self.rule)

    def evolve(self, steps):
        mapping = {0: '-', 1: '*'}
        for i in range(math.floor(steps)):
            print(''.join([mapping[s] for s in self.state]))
            self.state = self.rule(self.state)
