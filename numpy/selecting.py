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

print("______________________________________________________________")

print("Selecting part of a 2D array")
print("arr[ row indicies, column indicies]")

arr = np.array([[0, 1], [2, 3], [4, 5]])
print(arr)

print("\nThe first row:   arr[0, :]")
print(arr[0, :])
print(type(arr[0, :]))

print("\nThe second row:   arr[1, :]")
print(arr[1, :])

print("\nThe last row:   arr[-1, :]")
print(arr[1, :])

print("\nThe first column:   arr[:, 0]")
print(arr[:, 0])

print("\nThe second column:   arr[:, 1]")
print(arr[:, 1])


print("______________________________________________________________")

# Set up Earth with random values, representing different people.
# 25 random integers from 0..99
earth = np.random.randint(0, 100, 25)
earth = np.reshape(earth, (5,5))
print(earth)

# Place Waldo in a random location on Earth
WALDO = 1000
Waldo_location = (np.random.randint(5), np.random.randint(5))
print(Waldo_location)
print(type(Waldo_location))

earth[Waldo_location] = WALDO
print(earth)

# Find Waldo
Waldo_loc = np.nonzero(earth == WALDO)
print(Waldo_loc)

# np.nonzero( cond) returns a tuple
# The tuple contains np.ndim arrays.
# The first array tells which rows met the condition.
# The second array tells which columns met the condition.

# So Waldo_loc contains the row and column  where Waldo is.

# Let's confirm Waldo is there, by printing what is at the location
print(earth[Waldo_loc])
if earth[Waldo_loc] == WALDO:
    print("Found Waldo")

