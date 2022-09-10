import numpy as np

def get_aspected_index(two_pair_values, target_value): 
    arraysum = np.sum(np.array(two_pair_values), axis=1)
    result = np.where(arraysum == target_value)[0]
    return result

two_pair_values = [ [1, 5], [9, -7], [0, 8], [6, 3], [4, 11], [14, 0], [8, 1], [4, 9], ]
target_value = 9
result = get_aspected_index(two_pair_values, target_value) 
print(result)

