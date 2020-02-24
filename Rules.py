def apply_elementary_rule(rule_num):
    def apply_rule(state):
        mapping = {0: '-', 1: '*'}
        state = list(map(int, state))
        new_state = []
        rule = list(reversed(list(map(int, list(str(bin(rule_num))[2:].zfill(8))))))
        print(''.join([mapping[s] for s in state]))
        for index, cell in enumerate(state):
            if index == 0:
                new_state.append(rule[2 * state[index] + state[index + 1]])
            elif index == len(state) - 1:
                new_state.append(rule[4 * state[index - 1] + 2 * state[index]])
            else:
                new_state.append(rule[4 * state[index - 1] + 2 * state[index] + state[index + 1]])

        return new_state

    return apply_rule
