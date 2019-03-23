# Python Cheat Sheet

# Variables
x=5
x**2
x%2

x/2
x/float(2)

help(str)

# Strings
string1 = "ThisIsMyString"

string1*2
string1+'_NotYours'
'M' in string1

string1[4]
string1[6:]

string1.upper()
string1.lower()
string1.count('i')
string1.lower().count('i')
string1.replace('y','Y')
string1.strip()
string1.split('s')

# Lists
a = 'three'
b = 'four'
my_list = ['one','two', a, b]

my_list2 = [[1,2,3,4],[5,6,7,8]]

my_list[-2]
my_list2[-1]
my_list[1:3]
my_list[1:]
my_list[:3]

my_list[1][1]
my_list2[1][2]

my_list.index('two')
my_list2.count('one')
my_list.append('!')
my_list.remove('four')
del my_list[2]
my_list.reverse()
my_list.extend('!!')
my_list.pop(0)
my_list.insert(2,'!!!')
my_list.sort()

# Numpy Arrays
import numpy as np

py_list = [1, 2, 3, 4, 5]
np_array = np.array(py_list)
np_2darray = np.array([[1,2,3],[4,5,6]])

np_array[2]
np_array[0:2]
np_2darray[:,:2]

np_array > 2
np_array*2
np_array + np.array([2,2,2,2])

np_array.shape
np.append(np_array,5)
np.insert(np_array,1,100)
np.delete(np_array,1)
np.mean(np_array)
np.median(np_array)
np.std(np_array)
