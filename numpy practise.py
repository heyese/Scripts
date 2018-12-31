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
arr = np.full((3,3), True, dtype=bool)
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

