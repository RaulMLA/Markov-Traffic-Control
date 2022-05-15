"""Main module"""
from bellman_equation import BellmanEquations
from optimal_policy import OptimalPolicies


'''
REMARK:
The program will create states of length 3 (e.g., HHH, HHL, HLH, ...) with the items in STATES.
We can change the items in STATES and ACTIONS, but the length of states will be always 3.
Moreover, in the list GOAL_STATES, there can only be strings with length 3.
Note that COSTS keys must coincide with ACTIONS elements.
'''

# Constant lists representing the different states, actions and costs.
STATES = ['H', 'L']
ACTIONS = ['N', 'E', 'W']
GOAL_STATES = ['LLL']
COSTS = {'N': 20, 'E': 20, 'W': 20}

# Constant string representing the name of the csv file with the data.
FILE = "/Data.csv"



# -------------------------------------------------------------------------------------------- #
# --------------------------------<------ CALCULATIONS ------>-------------------------------- #
# -------------------------------------------------------------------------------------------- #

# We calculate the expected values using the Bellman Equation for MDPs.
expected_values = BellmanEquations(STATES, GOAL_STATES, ACTIONS, COSTS, FILE)

# We print the expected results of the Bellman Equation for MDPs.
print('\n\n\nRESULTS OF BELLMAN EQUATIONS\n----------------------------')
for key in expected_values:
    print('V({0}) = {1}' .format(key, expected_values[key]))


# We calculate the optimal policy.
optimal_policies = OptimalPolicies(STATES, GOAL_STATES, ACTIONS, COSTS, expected_values, FILE)

# We print the optimal policies for each state.
print('\n\n\nRESULTS OF OPTIMAL POLICIES\n---------------------------')
for key in optimal_policies:
    print('V({0}) = {1}' .format(key, optimal_policies[key]))
