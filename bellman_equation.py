#in order to have de probabilities dictionary
from probability_calculation import CalculateProbabilities


def BellmanEquation():
    # initialize the dictionaries to 0 in which dict1 contains every vi-1(s) and dict2 all vi(s)
    states, actions, probabilities = CalculateProbabilities()
    previous = {}
    current = {}
    bellman_states = []
    for initial_state_1 in states:
        for initial_state_2 in states:
            for initial_state_3 in states:
                state = initial_state_1 + initial_state_2 + initial_state_3
                previous[state] = 0
                current[state] = 0
                bellman_states.append(state)
                            
    i = 1   
    condition = False
    while not condition:
        for state in bellman_states:
            current[state] = bellman(state, bellman_states, probabilities, previous)
            if previous[state] != current[state]:
                previous[state] = current[state]
                current[state] = 0

        
        count = 0
        for key in previous:
            print('[{0}] Previous: {1}, Current: {2}' .format(i, previous[key], current[key]))
            if previous[key] == current[key]:
                count += 1
        if count == len(bellman_states):
            condition = True
            
        i += 1
    print('Iterations: ', (i - 1))
    return current
            



def bellman(s, bellman_states, probabilities, previous):
    results = []
    actions = ["N", "E", "W"]
    actions_cost = {"N": 1, "E": 1, "W": 1}
    for a in actions:
        r = actions_cost[a] + summatory(s, a, bellman_states, probabilities, previous)
        results.append(r)
    return min(results)       




def summatory(s, a, bellman_states, probabilities, previous):
    sum = 0
    for b in bellman_states:
        key = b + "|" + a + ',' + s
        sum = sum + probabilities[key]*previous[b]
    return round(sum, 6)    
    
