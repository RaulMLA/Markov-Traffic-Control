#in order to have de probabilities dictionary
from probability_calculation import CalculateProbabilities


def BellmanEquation():
    """Function which returns a dictionary with the expected values for each state V(S)"""
    states, actions, probabilities = CalculateProbabilities()
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
            current[state] = bellman(state, bellman_states, probabilities, previous)
            print('V({0}) = {1}' .format(state, current[state]))

        # We check if there are no changes in the previous and current dictionary.
        if previous == current:
            condition = True

        # We copy the content of current into previous to continue with the following operation.
        for state in bellman_states:
            previous[state] = current[state]
            
        i += 1
        
        '''if i == 4:
            condition = True'''
            
    print('\n\nTotal iterations: ', (i - 1))
    return current
            



def bellman(state, bellman_states, probabilities, previous):
    results = []
    actions = ["N", "E", "W"]
    actions_cost = {"N": 1, "E": 1, "W": 1}
    for action in actions:
        r = actions_cost[action] + summatory(state, action, bellman_states, probabilities, previous)
        results.append(round(r, 6))

    return min(results)




def summatory(state, action, bellman_states, probabilities, previous):
    """Function which calculates the summatory of the bellman equation: summatory[P(S'|a,S)*V(S)]"""
    sum = 0
    for b in bellman_states:
        key = b + "|" + action + ',' + state
        sum = sum + probabilities[key] * previous[b]
    return sum
