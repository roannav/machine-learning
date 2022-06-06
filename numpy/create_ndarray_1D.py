import numpy as np

print("\nsimple 1D array")
arr = np.array([1, 2, 3, 4])
print(arr)
print(type(arr))
print(arr.dtype)

print("\narray of 0s")
arr = np.zeros(10)
print(arr)
print(len(arr))
print(arr.dtype)

print("\narray of 1s")
arr = np.ones(5)
print(arr)
print("\nsize is the total number of elements in the array")
print(arr.size)

print("\nshape returns a tuple of ints, which tell you how many elements there are in each dimension")
#print("For 2D, the first number is the the number of rows")
print(arr.shape)

print("\nndim is rank (aka number of dimensions or axes)")
print(arr.ndim)

print("\nnumpy.empty(n) creates an array of length n with random values that depend on the memory state")
arr = np.empty(5)
print(arr)

print("\ncan specify dtype, when creating the ndarray")
arr = np.array([1.1, 1.2, 1.3], dtype=np.float64)
print(arr)
print(arr.dtype)

print("\nforce the floats to become ints")
arr = np.array([1.1, 1.2, 1.3], dtype=np.int64)
print(arr)
print(arr.dtype)

print("\nforce the ints to become floats")
arr = np.array([1, 2, 3], dtype=np.float64)
print(arr)
print(arr.dtype)
