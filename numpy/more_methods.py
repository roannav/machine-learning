import numpy as np

arr = np.random.randint(0, 10, 5)
print(arr)
print(type(arr))

# convert ndarray to a Python list
lst = arr.tolist()


# This doesn't make a copy;
# so changing one with change the other
arr2 = arr
arr[0] = 99
print(arr)
print(arr2)

# So now that arr3 is a copy,
# changing arr will not affect arr3, but will affect arr2
arr3 = np.copy(arr)
arr[0] = 20
print(arr)
print(arr2)
print(arr3)


# full of pi
arr.dtype = float
arr.fill( 3.14)
print(arr)

arr = np.random.rand(10)
print(arr)
print(arr.round(1))  # round all the floats to 1 decimal point


arr = np.random.randint(0, 10, 5)
print(arr)
print(f"min is {arr.min()}")
print(f"max is {arr.max()}")
print(f"index of min value is {arr.argmin()}")
print(f"index of max value is {arr.argmax()}")
print(f"sum of all the array elements is {arr.sum()}")
print(f"mean of all the array elements is {arr.mean()}")
print(f"variance of all the array elements is {arr.var()}")
print(f"standard deviation of all the array elements is {arr.std()}")

print(f"Do all elements evaluate to True? {arr.all()}")
print(f"Does any element evaluate to True? {arr.any()}")
