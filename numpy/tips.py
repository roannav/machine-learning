import numpy as np

# python arrays
arr1D = [3,2,8]

arr2D = [[5,0,7],
         [4,1,2]]
print("\nPython list: to represent a 2D array")
print(arr2D)
print(f"Type is {type(arr2D)}")  # type is list 
print(f"Length is {len(arr2D)}, because there are 2 rows.")

a = np.arange(15)
print("\nnumpy.ndarray: to represent a 1D array")
print(a)
print(f"Type is {type(a)}")  # type is ndarray
print(f"Shape is {a.shape}")
print(f"ndim (aka number of axes or dimensions) is {a.ndim}")
print("1 axis or 2+ axes")


a = a.reshape(3,5)
print("\nnumpy.ndarray: to represent a 2D array")
print(a)
# has 2 axes.
# first axis has length 3
# second axis has length 5
print(f"Shape is {a.shape}")
print(f"ndim (aka number of axes or dimensions) is {a.ndim}")
print("1 axis or 2+ axes")
print(f"Length is {len(a)}, because there are 3 rows.")


# Growing an array is inefficient;
# so it's better to create a large enough array.
# Fill it with placeholders by
# using np.zeros(), np.ones(), or np.empty()


# TIP: don't forget the []
#a = np.array( 3, 6, 9)   # Error
a = np.array([3, 6, 9])  # Correct

print(f"\nTIP: a Python list can hold a variety of types at the same time "
      f"within 1 list.")
lst = [ True, None, 'a', 33.3]
print(lst)

print(f"\nTIP: However, every element in the numpy.ndarray must have "
      f"the same type.")
# For example, they can be all numbers or all strings or all booleans.
print("\nnumpy.ndarray can also hold strings.")
a = np.array(['a', 'hi', 'the'])
print(a)

print("\nnumpy.ndarray can also hold booleans.")
a = np.array([True, False, True])
print(a)
