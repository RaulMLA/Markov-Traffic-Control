from bellman_equation import BellmanEquation

bellman_values = BellmanEquation()

print('\n\n\n##### RESULTS OF BELLMAN EQUATIONS #####')
for key in bellman_values:
    print('V({0}) = {1}' .format(key, bellman_values[key]))
