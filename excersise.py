x = ('rat', 'cat', 'leo', 'tiger', 'dog')      # tuple
y = {'bat', 'ball', 'shoe', 'net', 'god'}      # set
z = ['cake', 'cookies', 'crisp', 'candy']      # list
arr = [0, 1, 2, 31, 4, 51, 6, 71, 8, 9, 10]    # array

a = list(x)                                    # tuple converted to list
b = list(y)                                    # set converted to list
print('\n')

print('Converted from tuple to list : ', a,   type(a))
print('Converted from set to list   : ', b,   type(b))
print('Actual list defined          : ', z,   type(z))
print('Array elements               : ', arr, type(arr))

print('')
