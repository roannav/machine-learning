import numpy as np

# create a 2D array with integers 0..7.  4 rows and 2 columns.
arr1 = np.arange(8).reshape(4,2)
print(arr1)
print(f"Not surprisingly, since we just reshaped it, it has shape {arr1.shape}")

# create a 1D array with 7 random integers 1..9
arr2 = np.random.randint(1,10,7)
print(f"\nrandom numbers: {arr2}")
print(f"sorted: {np.sort(arr2)}")

print(f"The type of the elements in the array is {arr2.dtype}")

print(f"The dimensions (aka rank) is {arr2.ndim}")
print(f"It has shape {arr2.shape}")
print(f"It has size (aka total number of elements) of {arr2.size}")

# convert 1D array into a 2D row vector
row_vector = arr2[ np.newaxis, :]
print("\nrow vector")
print(row_vector)

print(f"The dimensions (aka rank) is {row_vector.ndim}")
print(f"It has shape {row_vector.shape}")
print(f"It has size {row_vector.size}\n")

# convert 1D array into a 2D column vector
col_vector = arr2[ :, np.newaxis]
print("\ncolumn vector")
print(col_vector)

print(f"The dimensions (aka rank) is {col_vector.ndim}")
print(f"It has shape {col_vector.shape}")
print(f"It has size {col_vector.size}\n")

for i in range(12):
    print(f"\nnp.linspace(0, 10, {i})")
    arr = np.linspace(0, 10, i)
    print(arr)


arr3 = arr.copy()
arr3[2:6] = 0
print(f"arr remains the same, because we made a copy: {arr}")
print(f"However, arr3 changes due to the assignment: {arr3}")
