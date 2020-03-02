def apply_rule(rule_num):
    def rule(state):
        state = list(map(int, state))
        new_state = []
        rule_bytes = list(reversed(list(map(int, list(str(bin(rule_num))[2:].zfill(8))))))

        for index, cell in enumerate(state):
            if index == 0:
                new_state.append(rule_bytes[2 * state[index] + state[index + 1]])
            elif index == len(state) - 1:
                new_state.append(rule_bytes[4 * state[index - 1] + 2 * state[index]])
            else:
                new_state.append(rule_bytes[4 * state[index - 1] + 2 * state[index] + state[index + 1]])
        return new_state

    return rule


class CellularAutomation:
    def __init__(self, rule_number):
        self.state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.rule = apply_rule(rule_number)

    def evolve(self, steps):
        mapping = {0: '-', 1: '*'}
        for i in range(steps):
            print(''.join([mapping[s] for s in self.state]))
            self.state = self.rule(self.state)


def main():
    automata = CellularAutomation(24)
    automata.evolve(10)


if __name__ == "__main__":
    main()
