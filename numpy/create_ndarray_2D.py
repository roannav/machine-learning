import numpy as np

arr = np.array([[1,2], [3,4], [5,6]])
print("\n", arr)
print(f"Number of dimensions is {arr.ndim}.")
print(f"How many elements in each dimension? {arr.shape}")
print("np.shape returns (num rows, num columns) for a 2D array.")
 
# choose random values bet 0..9
print("\nUse np.random.randint(n) to choose " + 
      "random ints between 0..(n-1)")
arr = np.random.randint(10, size=(3,2))
print(arr)
print(type(arr))
print("array size (aka total number of elements) " +
      f"is {arr.size}.\n")

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


print("__________________________________________________________")

arr = np.arange(8)
print("\n\nnp.arange(8)")
print(arr)
print(arr.shape)

print("\n\n2 ways to make a row vector:")

row_vector = arr[ np.newaxis, :]
print("\nrow_vector = arr[ np.newaxis, :]")
print(row_vector)
print(row_vector.shape)

row_vector2 = np.expand_dims(arr, axis=0)
print("\nrow_vector2 = np.expand_dims(arr, axis=0)")
print(row_vector2)
print(row_vector2.shape)

print("\n\n2 ways to make a column vector:")

col_vector = arr[ :, np.newaxis]
print("\ncol_vector = arr[ :, np.newaxis]")
print(col_vector)
print(col_vector.shape)

col_vector2 = np.expand_dims(arr, axis=1)
print("\ncol_vector2 = np.expand_dims(arr, axis=1)")
print(col_vector2)
print(col_vector2.shape)

