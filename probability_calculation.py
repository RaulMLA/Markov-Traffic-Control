"""Module for the calculation of the matrix of count_occurrencesd (transition function)."""

import os
import csv

def CalculateProbabilities():
    """Function for the calculations of count_occurrences (transition function)."""
    
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
    ACTIONS = ['N', 'E', 'W']

    # Real path of Data.csv to avoid problems during execution.
    FILE_NAME = "/Data.csv"
    DIR_PATH = os.path.dirname(os.path.realpath(__file__)) + FILE_NAME

    # Counts from the csv (two models: using a matrix and a dictionary).
    count_occurrences = []
    count_occurrences_dict = {}

    # Transition matrix (two models: using a matrix and a dictionary).
    probabilities_matrix = []
    probabilities = {}


    # Matrix which stores the data of the csv file.
    data = []

    # Total count_occurrences is the number of rows of the file.
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

    # Calculation of count_occurrences in the order specified in the report.
    for action in ACTIONS:
        for initial_state_1 in STATES:
            for initial_state_2 in STATES:
                for initial_state_3 in STATES:
                    for goal_state_1 in STATES:
                        for goal_state_2 in STATES:
                            for goal_state_3 in STATES:

                                # New row to count the occurrences in the csv file.
                                new_row = []

                                # count_occurrences order:
                                #print('P({0}{1}{2} / {3}, {4}{5}{6})' .format(states[goal_state_1], states[goal_state_2], states[goal_state_3], actions[action], states[initial_state_1], states[initial_state_2], states[initial_state_3]))

                                initial_traffic = initial_state_1 + initial_state_2 + initial_state_3
                                action_done = action
                                final_traffic = goal_state_1 + goal_state_2 + goal_state_3

                                new_row.append(initial_traffic)
                                new_row.append(action_done)
                                new_row.append(final_traffic)

                                count = data.count(new_row)

                                #print('\nCount is: {0}\nData is: {1}' .format(count, new_row))

                                counts.append(count)

                                # Testing data into a dictionary with the corresponding keys.
                                key = goal_state_1 + goal_state_2 + goal_state_3 + '|' \
                                + action + ',' + initial_state_1 + initial_state_2 + initial_state_3
                                count_occurrences_dict[key] = count
                                
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
    for item in count_occurrences_dict:
        print('Count({0}) = {1}'.format(item, count_occurrences_dict[item]))
    '''

    # Separation of counts into different lists to form a matrix (count_occurrences).
    counter = NUM_COLUMNS
    new_row = []

    for count in counts:
        if counter != 0:
            new_row.append(count)
            counter -= 1
        if counter == 0:
            count_occurrences.append(new_row)
            new_row = []
            counter = NUM_COLUMNS


    '''
    print('\n\n\nCsv counts matrix (Counts):')
    for row in count_occurrences:
        print(row)
    '''


    # Calculation of count_occurrences for each row of the matrix.
    row_counts = []
    for row in count_occurrences:
        row_count = 0
        for item in row:
            row_count += item
        
        row_counts.append(row_count)
        new_row = []
        
        if row_count != 0:
            for item in row:
                new_row.append(round((item / row_count), 6))
        else:
            for item in row:
                new_row.append(0)
        
        probabilities_matrix.append(new_row)

    

    # We calculate the probabilities and we store them in a dictionary (probabilities) which will be returned.
    index = 0
    counter = 0
    for key in count_occurrences_dict:
        probabilities[key] = round((count_occurrences_dict[key] / row_counts[index]), 6)
        counter += 1
        if counter == NUM_COLUMNS + 1:
            index += 1
    
    for key in probabilities:
        print("P({0}) = {1}" .format(key, probabilities[key]))


    '''
    # Print the final matrix with all the count_occurrences (transition matrix).
    print('\n\n\nTransitions matrix (count_occurrences):')
    for row in probabilities_matrix:
        print(row)
    '''


    # Return the set of states, the set of actions and the set of count_occurrences.
    return STATES, ACTIONS, probabilities


# Call the function.
CalculateProbabilities()
