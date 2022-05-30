# Comparing 2 functions from numpy:  arange() vs linspace()
import numpy as np

#############################################################################

# numpy.arange( start, stop, step)
# Just like in a for loop, step is the step size, 
# start is included, and stop is excluded.

# For integer arguments, numpy.arange() is just like Python range()

print("\nUsing numpy.arange()")
x = np.arange(10)   # 0..9
print(x)

x = np.arange(4,9)  # 4..8
print(x)

x = np.arange(1,11,2)  # odd numbers 1..9
print(x)


#############################################################################

# numpy.linspace( start, stop, num)
# num is number of samples to generate
# start and stop are included

# endpoint=False   #To exclude the stop value

print("\nUsing numpy.linspace()")
x = np.linspace(0,1, num=2)
print(x)

x = np.linspace(0,1, num=3)
print(x)

print("\nFor numpy.linspace(), the stop value is included by default")
print("np.linspace(0,1, num=4)")
x = np.linspace(0,1, num=4)
print(x)

print("\nFor numpy.linspace(), set 'endpoint=False' to exclude the stop value")
print("np.linspace(0,1, num=4, endpoint=False)")
x = np.linspace(0,1, num=4, endpoint=False)
print(x)

#############################################################################

print("\nComparing numpy.linspace() and numpy.arange()")
print("2 ways to make an nd_array with 0, 0.25, 0.5, 0.75, and 1")
x = np.linspace(0,1, num=5)
print(x)

x = np.arange(0, 1.1, 0.25)
print(x)

#############################################################################

print("\n2 ways to make an nd_array from 0 .. 100")
# numpy.linspace( start, stop, num)
# start and stop are included
x = np.linspace(0, 100, 11)
print(x)

# numpy.arange( start, stop, step)
# step is the step size, just like in a for loop
# start is included.  stop is excluded 
x = np.arange(0, 101, 10)
print(x)

#############################################################################

# src https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange
# WARNING: If the step is a float and dtype is int, then "Precision loss can occur here, due to casting or due to using floating points when start is much larger than step."
print("\nSome problems with np.arange() when step is a float and dtype is int")
x = np.arange(0, 5, 0.5, dtype=int)
print(x)

x = np.arange( -3, 3, 0.5, dtype=int)
print(x)

#############################################################################

# No problem here, since the dtype is inferred from the step=0.5, which is a float.
print("\nNo problems with np.arange() when step is a float and dtype is inferred to also be a float")
x = np.arange(0, 5, 0.5)
print(x)

# No problem here, since the dtype is inferred from the step=0.5, which is a float.
x = np.arange( -3, 3, 0.5)
print(x)

#############################################################################
