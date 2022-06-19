import numpy as np

# For a 1D array, numpy.argmin() returns the index of the min element 
# of the array

# The two 0s are the minimums
arr = [ 3, 0, 5, 0, 9, 2, 8]

# Find where the two 0s are
# Use axis=0 for a 1D array
min_locations = np.argmin( arr, axis=0)

# returns 1
# NOTE: it returns the index of the first minimum
print(min_locations)


#######################################################################

# For a 2D array, numpy.argmin() returns the indicies of the min element
# of the array

# The two 0s are the minimums
arr2D = [[3, 0, 5],
         [9, 2, 0]]


# Use axis=1, so find the minimum of each row. Then return their indicies.
min_locations = np.argmin( arr2D, axis=1)

# returns [1 2]
# It compares 3, 0, and 5.   0 is the least, so it returns 1 as the index. 
# It compares 9, 2, and 0.   0 is the least, so it returns 2 as the index. 
print(min_locations)


# Use axis=0, so find the minimum of each column. Then return their indicies.
min_locations = np.argmin( arr2D, axis=0)

# returns [0 0 1]
# It compares 3 and 9.   3 is less, so it returns 0 index. 
# It compares 0 and 2.   0 is less, so it returns 0 index. 
# It compares 5 and 0.   0 is less, so it returns 1 index. 
print(min_locations)


#######################################################################

arr2D = [[7, 3, -1],
         [5, 1,  1],
         [2, 8, -1]]


# Use axis=1, so find the minimum of each row.  Then return their indicies.
min_locations = np.argmin( arr2D, axis=1)

# returns [2,1,2]
# It compares 7, 3, and -1.  -1 is the least, so it returns 2 as the index. 
# It compares 5, 1, and  1.   1 is the least,  but we have a tie, so it
#    returns the first occurrence, so it returns 1 as the index. 
# It compares 2, 8, and -1.  -1 is the least, so it returns 2 as the index. 
print(min_locations)


# Use axis=0, so find the minimum of each column.  Then return their indicies.
min_locations = np.argmin( arr2D, axis=0)

# returns [2 1 0]
# It compares 7, 5, and 2.   2 is the least, so it returns 2 as the index. 
# It compares 3, 1, and 8.   1 is the least, so it returns 1 as the index. 
# It compares -1, 1, and -1.  -1 is the least, but we have a tie, so it
#    returns the first occurrence, so it returns 0 as the index. 
print(min_locations)


#######################################################################

# NOTE: If the input array is 2 dimensions or more, numpy.argmin() 
# always returns an array that has 1 less dimension than the input array.
# If the input array is 1 dimension, then numpy.argmin() returns a single
# number.
