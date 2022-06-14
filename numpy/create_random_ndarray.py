import matplotlib.pyplot as plt
import numpy as np

# initialize the pseudo random generator (MT19937 BitGenerator).
# This will cause the same stream of random number to be generated every time.
#np.random.seed(99)

#####################################################################
#
# random int
#
#####################################################################

# np.random.randint(end)
# excludes 'end'
# returns an integer
i = np.random.randint(1000)
print(i)

# np.random.randint(begin, end)
# includes 'begin', excludes 'end'
# returns an integer
i = np.random.randint(10,20)
print(i)

# np.random.randint(begin, end, num_samples)
# includes 'begin', excludes 'end'
# returns a 1D array
arr = np.random.randint(0,10,5)
print(arr)

# np.random.randint(begin, end, shape of array of samples)
# includes 'begin', excludes 'end'
# NOTE: the shape is in ()
# returns a 2D array
arr = np.random.randint(0,10,(3,4))
print(arr)


#####################################################################
#
# random float: [0,1)   uniform distribution
#
#####################################################################

# np.random.rand()
# returns a single float with value [0, 1)
f = np.random.rand()
print(f)

# np.random.rand( num_samples)
# returns an array of floats with length num_samples.
# Each float has values [0, 1)
arr = np.random.rand(5)
print(arr)

# np.random.rand( shape of array of samples)
# returns a 2D array of floats with values [0, 1)
arr = np.random.rand(3,5)     # 3 rows, 5 columns
print(arr)


#####################################################################
#
# random floats sampled from a Gaussian distribution (aka Normal distribution)
# By default, mean=0 and variance=1, so it's a standard normal distribution.
#
# normal() and randn() use the same normal distribution.
#
# However, normal() has parameters to set the mean (aka loc) 
# and variance (aka scale).
# numpy.random.normal( loc, scale, size)
#
#####################################################################

# np.random.randn( num_samples)
# random floats sampled from a standard normal distribution.
# returns an array of floats
y = np.random.randn(20)
print(y)

# np.random.rand( shape of array of samples)
# random floats sampled from a standard normal distribution.
# returns a 3D array of floats
arr = np.random.randn(2,3,4)
print(arr)

# graph a bunch of numbers that are around 100 
y = np.random.normal(100, 1, 20)
print(y)
plt.plot( np.arange(20), y)
plt.show()
