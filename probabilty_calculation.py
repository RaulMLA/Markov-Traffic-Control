"""Module for the calculation of the matrix of probabilitiesd (transition function)."""

import os
import csv

def CalculateProbabilities():
    """Function for the calculations of probabilities (transition function)."""
    
    # Definition of constants.
 
    # Number of rows and columns of the transition matrix.
    NUM_ROWS = 24
    NUM_COLUMNS = 8

    '''
    Possible states and actions.
    · Set of STATES:
        - 'H' -> 'High'
        - 'L' -> 'Low'
    · Set of ACTIONS:
        - 'N' -> 'North'
        - 'E' -> 'East'
        - 'W' -> 'West'
    '''
    STATES = ['H', 'L']
    NUM_STATES = len(STATES)
    ACTIONS = ['N', 'E', 'W']
    NUM_ACTIONS = len(ACTIONS)

    # Real path of Data.csv to avoid problems during execution.
    FILE_NAME = "/Data.csv"
    DIR_PATH = os.path.dirname(os.path.realpath(__file__)) + FILE_NAME

    # Probabilities (two models: using a matrix and a dictionary).
    probabilities = []
    data_dictionary = {}

    # Matrix which stores the data of the csv file.
    data = []

    # Total probabilities is the number of rows of the file.
    total_rows = 0
    
    # Data extraction from the csv file.
    with open(DIR_PATH, newline = '') as File:
        reader = csv.reader(File, delimiter = ";")
        for row in reader:
            # We skip the first row (header with titles).
            if total_rows != 0:
                new_row = []
                # e.g., row[0][0] takes the first letter (H or L) of the first field of the row (Initial traffic level N).
                initial_traffic = row[0][0] + row[1][0] + row[2][0]
                action = row[3]
                final_traffic = row[4][0] + row[5][0] + row[6][0]
                new_row.append(initial_traffic)
                new_row.append(action)
                new_row.append(final_traffic)
                data.append(new_row)

                '''
                # Information for debugging.
                #print('[\nROW %d]' %i)
                print('Initial traffic level N: ', row[0][0])
                print('Initial traffic level E: ', row[1][0])
                print('Initial traffic level W: ', row[2][0])
                print('Green traffic light: ', row[3])
                print('Final traffic level N: ', row[4][0])
                print('Final traffic level E: ', row[5][0])
                print('Final traffic level W: ', row[6][0])
                '''

            total_rows += 1

    total_rows -= 1

    '''
    # Print the matrix with all the data.
    for i in range(len(data)):
        print(data[i])
    '''

    # List which stores all the counts of the different rows of the csv file (all together).
    counts = []

    # Calculation of probabilities in the order specified in the report.
    for action in range(NUM_ACTIONS):
        for initial_state_1 in range(NUM_STATES):
            for initial_state_2 in range(NUM_STATES):
                for initial_state_3 in range(NUM_STATES):
                    for goal_state_1 in range(NUM_STATES):
                        for goal_state_2 in range(NUM_STATES):
                            for goal_state_3 in range(NUM_STATES):

                                # New row to count the occurrences in the csv file.
                                new_row = []

                                # Probabilities order:
                                #print('P({0}{1}{2} / {3}, {4}{5}{6})' .format(states[goal_state_1], states[goal_state_2], states[goal_state_3], actions[action], states[initial_state_1], states[initial_state_2], states[initial_state_3]))

                                initial_traffic = STATES[initial_state_1] + STATES[initial_state_2] + STATES[initial_state_3]
                                action_done = ACTIONS[action]
                                final_traffic = STATES[goal_state_1] + STATES[goal_state_2] + STATES[goal_state_3]

                                new_row.append(initial_traffic)
                                new_row.append(action_done)
                                new_row.append(final_traffic)

                                count = data.count(new_row)

                                #print('\nCount is: {0}\nData is: {1}' .format(count, new_row))

                                counts.append(count)

                                # Testing data into a dictionary with the corresponding keys.
                                key = STATES[goal_state_1] + STATES[goal_state_2] + STATES[goal_state_3] + '/' \
                                + ACTIONS[action] + ',' + STATES[initial_state_1] + STATES[initial_state_2] + STATES[initial_state_3]
                                data_dictionary[key] = count
                                
                                '''
                                # Information for debugging.
                                print(states[goal_state_1])
                                print(states[goal_state_2])
                                print(states[goal_state_3])
                                print(actions[action])
                                print(states[initial_state_1])
                                print(states[initial_state_2])
                                print(states[initial_state_3])
                                #print('List [{0}]: {1}' .format(i + 1, data[i]))
                                '''

    '''
    print('\n\n\nCount of rows from the csv file (using a dictionary):')
    for item in data_dictionary:
        print('Count({0}) = {1}'.format(item, data_dictionary[item]))
    '''

    # Separation of counts into different lists to form a matrix (probabilities).
    counter = NUM_COLUMNS
    new_row = []

    for count in counts:
        if counter != 0:
            new_row.append(count)
            counter -= 1
        if counter == 0:
            probabilities.append(new_row)
            new_row = []
            counter = NUM_COLUMNS


    print('\n\n\nCsv counts matrix (Counts):')
    for row in probabilities:
        print(row)


    # Calculation of probabilities for each row of the matrix.
    matrix = []

    for row in probabilities:
        row_count = 0
        for item in row:
            row_count += item
        
        new_row = []

        if row_count != 0:
            for item in row:
                new_row.append(round((item/row_count), 6))
        else:
            for item in row:
                new_row.append(0)
        
        matrix.append(new_row)


    # Print the final matrix with all the probabilities (transition matrix).
    print('\n\n\nTransitions matrix (Probabilities):')
    for row in matrix:
        print(row)

    # Return the set of states, the set of actions and the set of probabilities.
    return STATES, ACTIONS, probabilities


# Call the function.
CalculateProbabilities()
