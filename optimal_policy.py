"""Module for the calculation of the optimal policies."""
from probability_calculation import CalculateProbabilities


def OptimalPolicies(states: list, goal_states: list, actions: list, costs: dict, expected_values: dict, file: str) -> dict:
    """Function which calcualtes the optimal policies for a set of states"""

    optimal_policies = {}
    
    probabilities = CalculateProbabilities(states, actions, file)

    bellman_states = []
    # Initialize the dictionaries to 0 in which previous contains every v_(i-1)(s) and current all v_i(s).
    # Also, bellman_states is filled with all the possible states.
    for initial_state_1 in states:
        for initial_state_2 in states:
            for initial_state_3 in states:
                state = initial_state_1 + initial_state_2 + initial_state_3
                bellman_states.append(state)
    
    # We need the optimal policy for each key of the dictionary (different states).
    for state in bellman_states:
        # Dictionary with the result of applying Bellman to each state.
        results = {}

        for action in actions:
            if state in goal_states:
                results[action] = 0
            else:
                r = costs[action] + summatory(state, action, probabilities, expected_values, bellman_states)
                results[action] = round(r, 6)

        # Now, we take the minimum of the results list (optimal policy) and we put it into the results dictionary (optimal_policies).
        optimal_policy = min(results, key = results.get)
        optimal_policies[state] = optimal_policy

    # We remove the goal states from the optimal policies.
    for state in goal_states:
        if state in optimal_policies.keys():
            optimal_policies.pop(state)       
            
    # We return the dictionary with the optimal policy for each state.
    return optimal_policies
            
    
def summatory(state, action, probabilities, expected_values, bellman_states):
    """Function which calculates the summatory"""
    sum = 0
    for b in bellman_states:
        key = b + "|" + action + ',' + state
        sum = sum + (probabilities[key] * expected_values[b])
    return sum
    