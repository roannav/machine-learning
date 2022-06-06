import numpy as np

# np.random.randint(begin, end, num_samples)
# includes 'begin', excludes 'end'
# returns a 1D array
arr = np.random.randint(0, 100, 10)
print(arr)

# return sorted COPY of the array
print(np.sort(arr))

# return sorted COPY of the array, in reverse order
print(np.flip(np.sort(arr)))

# original array is unchanged
print(arr)
