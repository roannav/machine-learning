import numpy as np

# choose random values bet 0..9
arr = np.random.randint(10, size=(3,2))
print(arr)

'''
# Sample output
[[8 1]
 [8 7]
 [9 7]]
'''


# make a list 0..7
arr = np.arange(8).reshape(2, 4)
print(arr)

'''
# Output
[[0 1 2 3]
 [4 5 6 7]]
'''


# reshape the other way
arr = np.arange(8).reshape(4, 2)
print(arr)

'''
# Output
[[0 1]
 [2 3]
 [4 5]
 [6 7]]
'''


# vertically stack arrays
arr1 = np.array([1,2])
print(arr1)

arr2 = np.vstack((arr1, arr1))
print(arr2)

# horizontally stack arrays
arr3 = np.hstack((arr2, arr2))
print(arr3)
