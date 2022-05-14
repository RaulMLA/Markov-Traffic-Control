"""Module for the calculation of the matrix of count_occurrencesd (transition function)."""
import os
import csv


def CalculateProbabilities(states: list, actions: list, file: list) -> dict:
    """Function for the calculations of count_occurrences (transition function)."""
    # Definition of constants.

    # Number of rows and columns of the transition matrix.
    #NUM_ROWS = len(actions) * pow(len(states), 3)
    #NUM_COLUMNS = pow(len(states), 3)

    #print("Rows: ", NUM_ROWS)
    #print("Columns: ", NUM_COLUMNS)
    '''
    Possible states and actions.
    · Set of states:
        - 'H' -> 'High'
        - 'L' -> 'Low'
    · Set of actions:
        - 'N' -> 'North'
        - 'E' -> 'East'
        - 'W' -> 'West'
    '''

    # Real path of Data.csv to avoid problems during execution.
    DIR_PATH = os.path.dirname(os.path.realpath(__file__)) + file

    probabilities = {}

    # Matrix which stores the extracted data of the csv file.
    data = []

    # Total count_occurrences is the number of rows of the file.
    total_rows = 0

    # Calculation of all the possible combinations of states.
    possible_states = []
    for initial_state_1 in states:
        for initial_state_2 in states:
            for initial_state_3 in states:
                new_state = initial_state_1 + initial_state_2 + initial_state_3
                possible_states.append(new_state)

    # Data extraction from the csv file.
    with open(DIR_PATH, newline='') as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            # We skip the first row (header with titles).
            if total_rows != 0:
                # We create a string with the form <initial_state><action><goal_state> for each row of the file.
                initial_traffic = row[0][0] + row[1][0] + row[2][0]
                action = row[3]
                final_traffic = row[4][0] + row[5][0] + row[6][0]
                new_row = initial_traffic + action + final_traffic
                data.append(new_row)
            total_rows += 1

    total_rows -= 1
    
    '''# Print the matrix with all the data.
    for i in range(len(data)):
        print(data[i])'''
    
    # List which stores all the counts of the different rows of the csv file (all together).
    counts = []

    # We need to calculate the total count of each row S with the associated action to calculate the final probabilities.
    row_counts = {}
    for action in actions:
        for state_1 in possible_states:  
            limit = len(possible_states)
            counter = 0
            for state_2 in possible_states:
                element = state_1 + action + state_2
                counter += data.count(element)
                if limit == 1:
                    row_counts[state_1 + action] = counter
                    #print('Count of {0} is {1}' .format(element, counter))
                limit -= 1
    
    # Now we have to calculate the total probabilities for the transition matrix (allocated in a dictionary).
    for action in actions:
        for initial_state in possible_states:
            for final_state in possible_states:
                element = initial_state + action + final_state
                if row_counts[initial_state + action] == 0:
                    value = 0
                else:
                    value = data.count(element) / row_counts[initial_state + action]
                key = final_state + '|' + action + ',' + initial_state
                probabilities[key] = (value)
                #print('P({0}) = {1}/{2} = {3}' .format(key, data.count(element), row_counts[initial_state + action], value))

    return probabilities

#CalculateProbabilities()
