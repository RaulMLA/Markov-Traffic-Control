"""Module for the calculation of the expected values."""
from probability_calculation import CalculateProbabilities



def BellmanEquations(states: list, goal_states: list, actions: list,
                     costs: dict, file: str) -> dict:
    """Function which returns a dictionary with the expected values for each state V(S)"""
    probabilities = CalculateProbabilities(states, actions, file)
    previous = {}
    current = {}
    bellman_states = []
    # Initialize the dictionaries to 0 in which previous contains every v_(i-1)(s) and current all v_i(s).
    # Also, bellman_states is filled with all the possible states.
    for initial_state_1 in states:
        for initial_state_2 in states:
            for initial_state_3 in states:
                state = initial_state_1 + initial_state_2 + initial_state_3
                previous[state] = 0
                current[state] = 0
                bellman_states.append(state)

    i = 1
    # When condition is True, the iterations to find the expected values have finished (and they have been found).
    condition = False
    while not condition:
        print('\nIteration ', i)
        print('----------------')
        for state in bellman_states:
            if state in goal_states:
                current[state] = 0
            else:
                current[state] = bellman(state, actions, bellman_states, probabilities,
                                         previous, costs)
            print('V({0}) = {1}'.format(state, current[state]))

        # We check if there are no changes in the previous and current dictionary.
        if previous == current:
            condition = True

        # We copy the content of current into previous to continue with the following operation.
        for state in bellman_states:
            previous[state] = current[state]

        i += 1

        # For debugging purposes:
        if i == 4:
            condition = True

    print('\n\nTotal iterations: ', (i - 1))
    return current


def bellman(state, actions, bellman_states, probabilities, previous, actions_cost):
    results = []
    for action in actions:
        r = actions_cost[action] + summatory(state, action, bellman_states,
                                             probabilities, previous)
        results.append(round(r, 6))

    return min(results)


def summatory(state, action, bellman_states, probabilities, previous):
    """Function which calculates the summatory of the bellman equation: summatory[P(S'|a,S)*V(S)]"""
    sum = 0
    for b in bellman_states:
        key = b + "|" + action + ',' + state
        sum = sum + probabilities[key] * previous[b]
    return sum
