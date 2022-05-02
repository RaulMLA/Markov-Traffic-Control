# https://github.com/sachinbiradar9/Markov-Decision-Processes/blob/master/mdp.py

import os
import csv

# Path of Data.csv
dir_path = os.path.dirname(os.path.realpath(__file__)) + "/Data.csv"
# print("Real path: ", dir_path)

# Constants.
NUM_ROWS = 24
NUM_COLUMNS = 8

data = []
total_rows = 0
 
 # Data extraction from the csv file.
with open(dir_path, newline = '') as File:  
    reader = csv.reader(File, delimiter = ";")
    for row in reader:
        if total_rows != 0:
            new_row = []
            initial_traffic = row[0][0] + row[1][0] + row[2][0]
            action = row[3]
            final_traffic = row[4][0] + row[5][0] + row[6][0]
            new_row.append(initial_traffic)
            new_row.append(action)
            new_row.append(final_traffic)
            data.append(new_row)
            '''
            print('[\nROW %d]' %i)
            print('Initial traffic level N: ', row[0])
            print('Initial traffic level E: ', row[1])
            print('Initial traffic level W: ', row[2])
            print('Green traffic light: ', row[3])
            print('Final traffic level N: ', row[4])
            print('Final traffic level E: {1}', row[5])
            print('Final traffic level W: {1}', row[6])
            '''

        total_rows += 1

# There are 8785 samples in the data file.
total_rows -= 1
#print(total_rows)

# Print the matrix with all the data.
'''
for i in range(len(data)):
    print(data[i])
'''

# Possible states and actions.
states = ['H', 'L']
actions = ['N', 'E', 'W']
counts = []

# Calculation of probabilities.
for goal_state_1 in range(len(states)):
    for goal_state_2 in range(len(states)):
        for goal_state_3 in range(len(states)):
            for action in range(len(actions)):
                for initial_state_1 in range(len(states)):
                    for initial_state_2 in range(len(states)):
                        for initial_state_3 in range(len(states)):

                            new_row = []

                            initial_traffic = states[initial_state_1] + states[initial_state_2] + states[initial_state_3]
                            action_done = actions[action]
                            final_traffic = states[goal_state_1] + states[goal_state_3] + states[goal_state_2]

                            new_row.append(initial_traffic)
                            new_row.append(action_done)
                            new_row.append(final_traffic)

                            count = data.count(new_row)

                            #print('\nCount is: {0}\nData is: {1}' .format(count, new_row))

                            counts.append(count)
                            
                            
                            '''
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
# Check if the number of items counted is OK.
count = 0
for item in counts:
    count += item
print(counts)
print('Expected count: {0}\nReal count: {1}' .format(total_rows, count))
'''


# Separation of counts into different lists to form a matrix (probabilities).
counter = NUM_COLUMNS
new_row = []
probabilities = []


for count in counts:
    if counter != 0:
        new_row.append(count)
        counter -= 1
    if counter == 0:
        probabilities.append(new_row)
        new_row = []
        counter = NUM_COLUMNS
        
for row in probabilities:
    print(row)

# Calculation of probabilities for each row of the matrix.
matrix = []

for row in probabilities:
    row_count = 0
    for item in row:
        row_count += item
    
    new_row = []
    for item in row:
        new_row.append(round((item/row_count), 6))
    
    matrix.append(new_row)


# Print the final matrix with all the probabilities (transition matrix).
for row in matrix:
    print(row)


# Initialization of the matrix of probabilities to 0.
for i in range(23):
    probabilities.append([])
    for j in range(7):
        probabilities[i].append(0)

'''
# Printing of the probabilities matrix.
for i in range(len(probabilities)):
    print(probabilities[i])
'''



'''
# Matrix (nested lists) where i are the rows (24 possible) and j the columns (8 possible).
probabilities = []

# Initialization of the matrix of probabilities to 0.
for i in range(24):
    probabilities.append([])
    for j in range(8):
        probabilities[i][j] = 0


# Another way would be define variables (inefficcient).
hhh_e_hhh = 0
hhl_e_hhh = 0
hlh_e_hhh = 0
hll_e_hhh = 0

for i in range(len(data)):
    for j in range(7):
        if data[i][0] == 'High' and data[i][1] == 'High' and data[i][2] == 'High' and data[i][3] == 'N' and data[i][4] == 'High' and data[i][5] == 'High' and data[i][6] == 'High':
            hhh_e_hhh += 1
        elif data[i][0] == 'High' and data[i][1] == 'High' and data[i][2] == 'Low' and data[i][3] == 'N' and data[i][4] == 'High' and data[i][5] == 'High' and data[i][6] == 'High':
            hhl_e_hhh += 1
        elif data[i][0] == 'High' and data[i][1] == 'Low' and data[i][2] == 'High' and data[i][3] == 'N' and data[i][4] == 'High' and data[i][5] == 'High' and data[i][6] == 'High':
            hlh_e_hhh += 1
        elif data[i][0] == 'High' and data[i][1] == 'Low' and data[i][2] == 'Low' and data[i][3] == 'N' and data[i][4] == 'High' and data[i][5] == 'High' and data[i][6] == 'High':
            hll_e_hhh += 1

print(round((hhh_e_hhh/counter), 6))
'''


# !!! Meter todo en esta función cuando funcione.
def CalculateProbabilities():

    # Possible states and actions.
    states = ['High', 'Low']
    actions = ['N', 'E', 'W']

    # Probabilities matrix.
    probabilities = []

    return states, actions, probabilities