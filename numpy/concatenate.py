import numpy as np

arr1 = np.arange(5)
print(arr1)

arr2 = np.arange(5,10)
print(arr2)

print("\nconcatenate a *tuple* of 2 arrays")
# NOTE: we are passing a *tuple* of 2 arrays
arr3 = np.concatenate((arr1, arr2))
print(arr3)

print("\nreshape, so array has 5 rows and 2 columns")
arr4 = arr3.reshape(5,2)
print(arr4)

# NOTE: the double [[ ]], so it's a 2D array
arr10 = np.array([[10,11]])
print("\n")
print(arr10)
print(f"has {arr10.shape[0]} row and {arr10.shape[1]} columns")

print("\nconcatenate a tuple of 2 arrays")
print("axis=0 is the default")
arr5 = np.concatenate((arr4, arr10)) 
print(arr5)

arr12 = np.array([[12,13]])
print("\nconcatenate a tuple of 2 arrays")
arr6 = np.concatenate((arr4, arr12), axis=0)
print(arr6)


# can't concat in that direction
#arr6 = np.concatenate((arr4, arr12), axis=1)

print("_______________________________________________")

print("\nreshape, so array has 2 rows and 5 columns")
arr7 = arr4.reshape(2,5)
print(arr7)

print("\n")
print(arr10)
print(f"has {arr10.shape[0]} row and {arr10.shape[1]} columns")

# This also doesn't work because arr10 is in the wrong shape
#arr8 = np.concatenate((arr7, arr10), axis = 1)
print(f"\nYou can't concatenate a 5x2 array with a 2x1 array")

print("\nreshape, so array has 2 rows and 1 column")
arr11 = arr10.reshape(2,1)
print(arr11)

print(f"\nNow, you can concatenate a 5x2 array with a 1x2 array")

print("\nconcatenate a tuple of 2 arrays.  axis=1")
arr8 = np.concatenate((arr7, arr11), axis = 1)
print(arr8)

print("\nreshape, so it's a 2D array that has 1 row.")
#arr13 = arr8.reshape(1)  # fails
arr13 = arr8.reshape(1, arr8.size)
print(arr13)

print("\nflatten, so it's a 1D array.")
arr13 = arr8.flatten()
print(arr13)

print("_______________________________________________")

arr1 = np.arange(5)   # 0..4
arr2 = arr1 + 5       # 5..9
print(arr1)
print(arr2)

arr3 = np.concatenate((arr1, arr2))  # axis = 0
print(arr3)

# causes numpy.AxisError: axis 1 is out of bounds for array of dimension 1
# Because it's a 1D array, there is no axis 1
#arr4 = np.concatenate((arr1, arr2), axis=1)
#print(arr4)

print("\nConvert the 1D arrays to 2D arrays")
arr5 = np.array([arr1])
print(arr5)

arr6 = np.array([arr2])
print(arr6)
print(f"has {arr6.shape[0]} row and {arr6.shape[1]} columns, so it's a {arr6.shape[1]}x{arr6.shape[0]} array")

# This time no error. 
# Because it's a 2D array, there is an axis 1
print("\nconcatenate the 2 2D arrays.  axis=1")
arr4 = np.concatenate((arr5, arr6), axis=1)
print(arr4)

print("\nconcatenate the 2 2D arrays.  axis=0")
arr3 = np.concatenate((arr5, arr6))  # axis = 0
print(arr3)

