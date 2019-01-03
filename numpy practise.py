import numpy as np

# https://www.machinelearningplus.com/python/101-numpy-exercises-python/

print('\n#1:')
print(f'Numpy version: {np.__version__}')

print('\n\n#2')
ndarr = np.arange(10)
print(ndarr.__repr__())

print('\n\n#3')
arr = np.fromiter((True for i in range(9)), bool, count=9).reshape(3, 3)
# Or, preferably:
arr = np.full((3, 3), True, dtype=bool)
# Or:
arr = np.ones((3, 3), dtype=bool)
print(arr.__repr__())

print('\n\n#4')
arr = np.arange(10)
arr_odd = arr[arr % 2 != 0]
print(arr_odd.__repr__())

print('\n\n#5')
arr = np.arange(10)
arr[arr % 2 == 1] = -1
print(arr.__repr__())

print('\n\n#6')
arr = np.arange(10)
arr3 = np.where(arr % 2 == 1, -1, arr)
print(arr3.__repr__())

print('\n\n#7')
arr = np.arange(10)
arr = arr.reshape(2, 5)
# Or use -1 to automatically set the right number for the unknown dimension
arr = arr.reshape(2, -1)
print(arr.__repr__())

print('\n\n#8')
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
# My first desperate attempt, which uses list comprehensions and unpacking ...
arr = np.array([i for i in [*a, *b]])
# But much better to stay with numpy functions:
arr = np.vstack((a, b))
# or
arr = np.concatenate((a, b), axis=0)

print('\n\n#9')
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
np.concatenate((a, b), axis=1)
np.hstack((a, b))

print('\n\n#10')
arr = np.arange(1,4)
np.hstack((np.repeat(arr, 3), np.concatenate((arr,)*3)))
# or
np.hstack((np.repeat(arr, 3), np.tile(arr, 3)))

print('\n\n#11')
# Common items
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
# Dropping back into pure python:
np.array(list(set(a.tolist()).intersection(set(b.tolist()))))
# Using the numpy function!
np.array(list(set(a.tolist()).intersection(set(b.tolist()))))
# Strangely, dropping to python in this case was much quicker ...

print('\n\n#12')
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
# My first attempt!
a[np.where(np.isin(a,b), np.zeros(b.size), np.ones(b.size)).astype(bool)]
# Ah - can use 'invert' to flip partity between True / False:
a[np.invert(np.isin(a,b))]
# I prefer my solution, actually, but given solution is useful to know.
# This returns a sorted, unique values from a that are not in b
np.setdiff1d(a,b)

print('\n\n#13')
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
# First attempt - used arange to get an array of indexes
np.arange(a.size)[a==b]
# But can simply use where ...
np.where(a==b)


