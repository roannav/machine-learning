import numpy as np

# a 1D array of 10 integers 0..9
arr = np.random.randint(0,10,10)
print("\nOriginal array:\n", arr, '\n')

# index and slice will return an ndarray
last3 = arr[-3:]
print(last3)
print(type(last3), '\n')  # ndarray

# use condition to select only some elements in the array
print(arr[ arr > 5 ])
result = arr[ arr > 5 ]
print(type(result), '\n')  # ndarray

cond = (arr < 3)
print(arr[cond])

# for each element in the array, print true or false,
# whether it satisfies the condition.
print(cond, '\n')

# compound conditions
cond = (arr < 2) | (arr == 9)   # very low or very high
print(arr[cond])
print(cond, '\n')

cond = (3 < arr) & (arr < 7)    # near the middle only
print(arr[cond])
print(cond, '\n')
