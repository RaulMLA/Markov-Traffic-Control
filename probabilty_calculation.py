import os

# Path of Data.csv
dir_path = os.path.dirname(os.path.realpath(__file__)) + "/Data.csv"
# print("Real path: ", dir_path)


import csv

data = []
counter = 0
 
with open(dir_path, newline = '') as File:  
    reader = csv.reader(File, delimiter = ";")
    for row in reader:
        if counter != 0:
            data.append(row)
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

        counter += 1

# There are 8785 samples in the data file.
counter -= 1
print(counter)

# Possible states and actions.
states = ['High', 'Low']
actions = ['N', 'E', 'W']

# Calculation of probabilities.
for i in range(len(data)):
    for goal_state_1 in range(len(states)):
        for goal_state_2 in range(len(states)):
            for goal_state_3 in range(len(states)):
                for action in range(len(actions)):
                    for initial_state_1 in range(len(states)):
                        for initial_state_2 in range(len(states)):
                            for initial_state_3 in range(len(states)):
                                if data[i][0] == states[goal_state_1] and data[i][1] == states[goal_state_2] and data[i][2] == states[goal_state_3] and data[i][3] == actions[action] and data[i][4] == states[initial_state_1] and data[i][5] == states[initial_state_2] and data[i][6] == states[initial_state_3]:
                                    '''
                                    print(states[goal_state_1])
                                    print(states[goal_state_2])
                                    print(states[goal_state_3])
                                    print(actions[action])
                                    print(states[initial_state_1])
                                    print(states[initial_state_2])
                                    print(states[initial_state_3])
                                    print('List [{0}]: {1}' .format(i + 1, data[i]))
                                    '''

# Matrix (nested lists) where i are the rows (24 possible) and j the columns (8 possible).
probabilities = []

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
