# Day 24: 30 Days of Python Programming

# importing numpy
import numpy as np 
# How to check the version of the numpy package
print('numpy:', np.__version__) #numpy: 1.26.2
# Checking the available methods
print(dir(np)) # ['ALLOW_THREADS', 'BUFSIZE', 'CLIP', 'DataSource', 'ERR_CALL', 'ERR_DEFAULT', 'ERR_IGNORE', 'ERR_LOG',....'zeros_like']

# Creating python List
python_list = [1,2,3,4,5]

# Checking data types
print('Type:', type (python_list)) # <class 'list'>
    
print(python_list) # [1, 2, 3, 4, 5]

two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]

print(two_dimensional_list)  # [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# Creating Numpy(Numerical Python) array from python list

numpy_array_from_list = np.array(python_list)
print(type (numpy_array_from_list))   # <class 'numpy.ndarray'>
print(numpy_array_from_list) # array([1, 2, 3, 4, 5])

# Creating float numpy arrays
# Creating a float numpy array from list with a float data type parameter
python_list = [1,2,3,4,5]

numy_array_from_list2 = np.array(python_list, dtype=float)
print(numy_array_from_list2) # [1. 2. 3. 4. 5.])

numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array) # array([False,  True,  True, False, False])

# Creating a boolean a numpy array from list
numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array) # [False  True  True False False]

# Creating multidimensional array using numpy
# A numpy array may have one or multiple rows and columns
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type (numpy_two_dimensional_list)) #<class 'numpy.ndarray'>
print(numpy_two_dimensional_list) 
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''

# Converting numpy array to list
# We can always convert an array back to a python list using tolist().
np_to_list = numpy_array_from_list.tolist()
print(type (np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())
'''
    <class 'list'>
    one dimensional array: [1, 2, 3, 4, 5]
    two dimensional array:  [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
'''

# Numpy array from tuple
# Creating tuple in Python
python_tuple = (1,2,3,4,5)
print(type (python_tuple)) # <class 'tuple'>
print('python_tuple: ', python_tuple) # python_tuple:  (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple)) # <class 'numpy.ndarray'>
print('numpy_array_from_tuple: ', numpy_array_from_tuple) # numpy_array_from_tuple:  [1 2 3 4 5]

# Shape of numpy array
# The shape method provide the shape of the array as a tuple. The first is the row and the second is the column. If the array is just one dimensional it returns the size of the array.

nums = np.array([1, 2, 3, 4, 5])
print(nums) #[1 2 3 4 5]
print('shape of nums: ', nums.shape) #shape of nums:  (5,)
print(numpy_two_dimensional_list)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape) #shape of numpy_two_dimensional_list:  (3, 3)
three_by_four_array = np.array([[0, 1, 2, 3],
        [4,5,6,7],
        [8,9,10, 11]])
print(three_by_four_array.shape) #(3, 4)

# Data type of numpy array
# Type of data types: str, int, float, complex, bool, list, None

int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array) # [-3 -2 -1  0  1  2  3]
print(int_array.dtype) # int32
print(float_array) # [-3. -2. -1.  0.  1.  2.  3.]
print(float_array.dtype) # float64

# Size of a numpy array
# In numpy to know the number of items in a numpy array list we use size

numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                              [3, 4, 5],
                              [6, 7, 8]])

print('The size:', numpy_array_from_list.size) # The size: 5
print('The size:', two_dimensional_list.size) # The size: 9

# Mathematical Operation using numpy
# Addition
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list) # original array:  [1 2 3 4 5]
ten_plus_original = numpy_array_from_list  + 10
print(ten_plus_original) # [11 12 13 14 15]

# Subtraction
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list) # original array:  [1 2 3 4 5]
ten_minus_original = numpy_array_from_list  - 10
print(ten_minus_original) # [-9 -8 -7 -6 -5]

# Multiplication
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list) # original array:  [1 2 3 4 5]
ten_times_original = numpy_array_from_list * 10
print(ten_times_original) # [10 20 30 40 50]

# Division
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list) # original array:  [1 2 3 4 5]
ten_times_original = numpy_array_from_list / 10
print(ten_times_original) # [0.1 0.2 0.3 0.4 0.5]

# Modulus; Finding the remainder
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list) # original array:  [1 2 3 4 5]
ten_times_original = numpy_array_from_list % 3
print(ten_times_original) # [1 2 0 1 2]

# Floor division: the division result without the remainder
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list) # original array:  [1 2 3 4 5]
ten_times_original = numpy_array_from_list // 10
print(ten_times_original) # [0 0 0 0 0]

# Exponential is finding some number the power of another:
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
print('original array: ', numpy_array_from_list) # original array:  [1 2 3 4 5]
ten_times_original = numpy_array_from_list  ** 2
print(ten_times_original) # [ 1  4  9 16 25]

#Int,  Float numbers
numpy_int_arr = np.array([1,2,3,4])
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')

print(numpy_int_arr.dtype) # int32
print(numpy_float_arr.dtype) # float64
print(numpy_bool_arr.dtype) # bool

# Converting types
# We can convert the data types of numpy array

# Int to Float
numpy_int_arr = np.array([1,2,3,4], dtype = 'float')
numpy_int_arr # array([1., 2., 3., 4.])

# Float to Int
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
numpy_int_arr # array([1, 2, 3, 4])

# Int ot boolean
np.array([-3, -2, 0, 1,2,3], dtype='bool') # array([ True,  True, False,  True,  True,  True])

# Int to str
numpy_float_list = np.array([1.2, 3.4, 5.6])
numpy_float_list.astype('int').astype('str') # array(['1', '3', '5'], dtype='<U11')

# Multi-dimensional Arrays
# 2 Dimension Array
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array)) #<class 'numpy.ndarray'>
print(two_dimension_array) 
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
''' 
print('Shape: ', two_dimension_array.shape) # Shape:  (3, 3)
print('Size:', two_dimension_array.size) # Size: 9
print('Data type:', two_dimension_array.dtype) # Data type: int32

# 2 Dimension Array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_row = two_dimension_array[0]
second_row = two_dimension_array[1]
third_row = two_dimension_array[2]
print('First row:', first_row) # First row: [1 2 3]
print('Second row:', second_row) # Second row: [4 5 6]
print('Third row: ', third_row) # Third row:  [7 8 9]
print(two_dimension_array)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

# Slicing Numpy array
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)
'''
[[1 2]
 [4 5]]
''' 

# How to reverse the rows and the whole array?
two_dimension_array[::]
'''
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
'''

# Reverse the row and column positions
two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
two_dimension_array[::-1,::-1]
'''
array([[9, 8, 7],
       [6, 5, 4],
       [3, 2, 1]])
'''

# How to represent missing values ?
print(two_dimension_array)
two_dimension_array[1,1] = 55
two_dimension_array[1,2] =44
print(two_dimension_array)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]

[[ 1  2  3]
 [ 4 55 44]
 [ 7  8  9]]
'''

# Numpy Zeroes
# numpy.zeros(shape, dtype=float, order='C')
numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
numpy_zeroes
''' 
array([[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]])
'''

# Reshape
# numpy.reshape(), numpy.flatten()
first_shape  = np.array([(1,2,3), (4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3,2)
print(reshaped)
'''
[[1 2 3]
 [4 5 6]]

[[1 2]
 [3 4]
 [5 6]]
'''
flattened = reshaped.flatten()
flattened # array([1, 2, 3, 4, 5, 6])

 # Horitzontal Stack
np_list_one = np.array([1,2,3])
np_list_two = np.array([4,5,6])

print(np_list_one + np_list_two) #[5 7 9]

print('Horizontal Append:', np.hstack((np_list_one, np_list_two))) #Horizontal Append: [1 2 3 4 5 6]

# Vertical Stack
print('Vertical Append:', np.vstack((np_list_one, np_list_two)))
'''
Vertical Append: [[1 2 3]
 [4 5 6]]
'''

# Generating Random Numbers
# Generate a random float  number
random_float = np.random.random()
random_float #0.03050148727452595
    
# Generate a random float  number
random_floats = np.random.random(5)
random_floats
# array([0.5395348 , 0.81517724, 0.64167769, 0.78004092, 0.53730221])

# Generating a random integers between 0 and 10
random_int = np.random.randint(0, 11)
random_int #2

# Generating a random integers between 2 and 11, and creating a one row array
random_int = np.random.randint(2,10, size=4)
random_int # array([6, 3, 6, 2])

# Generating a random integers between 0 and 10
random_int = np.random.randint(2,10, size=(3,3))
random_int
'''
array([[5, 3, 6],
       [8, 5, 8],
       [2, 3, 5]])
'''

# np.random.normal(mu, sigma, size)
normal_array = np.random.normal(79, 15, 80)
normal_array

# Matrix in numpy
four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
four_by_four_matrix
'''
matrix([[1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.]])
'''

# creating list using range(starting, stop, step)
lst = range(0, 11, 2)
lst # range(0, 11, 2)

for l in lst:
    print(l)
'''
0
2
4
6
8
10
'''

# Similar to range arange numpy.arange(start, stop, step)
whole_numbers = np.arange(0, 20, 1)
whole_numbers
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,      
       #17, 18, 19])

# Creating sequence of numbers using linspace
# numpy.linspace()
# numpy.logspace() in Python with Example
# For instance, it can be used to create 10 values from 1 to 5 evenly spaced.
np.linspace(1.0, 5.0, num=10)
'''
array([1.        , 1.44444444, 1.88888889, 2.33333333, 2.77777778,
       3.22222222, 3.66666667, 4.11111111, 4.55555556, 5.        ])
'''

# not to include the last value in the interval
np.linspace(1.0, 5.0, num=5, endpoint=False)
'''
array([1. , 1.8, 2.6, 3.4, 4.2])
'''

# LogSpace
# LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.

# Syntax:

# numpy.logspace(start, stop, num, endpoint)

np.logspace(2, 4.0, num=4)
# array([  100.        ,   464.15888336,  2154.43469003, 10000.        ])

# to check the size of an array
x = np.array([1,2,3], dtype=np.complex128)
x
#array([1.+0.j, 2.+0.j, 3.+0.j])
x.itemsize #16

# indexing and Slicing NumPy Arrays in Python
np_list = np.array([(1,2,3), (4,5,6)])
np_list
'''
array([[1, 2, 3],
       [4, 5, 6]])
'''

print('First row: ', np_list[0]) # First row:  [1 2 3]
print('Second row: ', np_list[1]) # Second row:  [4 5 6]

print('First column: ', np_list[:,0]) # First column:  [1 4]
print('Second column: ', np_list[:,1]) # Second column:  [2 5] 
print('Third column: ', np_list[:,2]) # Third column:  [3 6]

# NumPy Statistical Functions with Example
np_normal_dis = np.random.normal(5, 0.5, 100)
np_normal_dis
## min, max, mean, median, sd
print('min: ', two_dimension_array.min()) # min:  1
print('max: ', two_dimension_array.max()) # max:  55
print('mean: ',two_dimension_array.mean()) # mean:  14.777777777777779
# print('median: ', two_dimension_array.median())
print('sd: ', two_dimension_array.std()) # sd:  18.913709183069525

print(two_dimension_array)
'''
[[ 1  2  3]
 [ 4 55 44]
 [ 7  8  9]]
'''
print('Column with minimum: ', np.amin(two_dimension_array,axis=0)) # Column with minimum:  [1 2 3]
print('Column with maximum: ', np.amax(two_dimension_array,axis=0)) # Column with maximum:  [ 7 55 44]
print('=== Row ==') # === Row ==
print('Row with minimum: ', np.amin(two_dimension_array,axis=1)) # Row with minimum:  [1 4 7]
print('Row with maximum: ', np.amax(two_dimension_array,axis=1)) # Row with maximum:  [ 3 55  9]

# How to create repeating sequences?
a = [1,2,3]

# Repeat whole of 'a' two times
print('Tile:   ', np.tile(a, 2)) # Tile:    [1 2 3 1 2 3]

# Repeat each element of 'a' two times
print('Repeat: ', np.repeat(a, 2)) # Repeat:  [1 1 2 2 3 3]

# How to generate random numbers
# One random number between [0,1)
one_random_num = np.random.random()
one_random_in = np.random
print(one_random_num) # 0.19002881794566684

# Random numbers between [0,1) of shape 2,3
r = np.random.random(size=[2,3])
print(r)
'''
[[0.20045796 0.45253425 0.49369581]
 [0.90945092 0.20465493 0.6652243 ]]
'''

print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10)) # ['e' 'e' 'i' 'e' 'a' 'u' 'a' 'i' 'a' 'i']

rand2 = np.random.randn(2,2)
rand2
'''
array([[-3.09112016,  0.52501285],
       [-0.89838609, -0.30187242]])
'''

from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))

'''
    min:  3.557811005458804
    max:  6.876317743643499
    mean:  5.035832048106663
    median:  5.020161980441937
    mode:  ModeResult(mode=array([3.55781101]), count=array([1]))
    sd:  0.489682424165213

'''
import matplotlib.pyplot as plt
plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()

# Linear algebra
# Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,3])
np.dot(f, g)  # 23

# NumPy Matrix Multiplication with np.matmul()
# Matmul: matruc product of two arrays
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
np.matmul(h, i)
'''
    array([[19, 22],
           [43, 50]])
'''
# Determinant 2*2 matrix
np.linalg.det(i)
-1.999999999999999
Z = np.zeros((8,8))
Z[1::2,::2] = 1
Z[::2,1::2] = 1
Z

'''
array([[0., 1., 0., 1., 0., 1., 0., 1.],
       [1., 0., 1., 0., 1., 0., 1., 0.],
       [0., 1., 0., 1., 0., 1., 0., 1.],
       [1., 0., 1., 0., 1., 0., 1., 0.],
       [0., 1., 0., 1., 0., 1., 0., 1.],
       [1., 0., 1., 0., 1., 0., 1., 0.],
       [0., 1., 0., 1., 0., 1., 0., 1.],
       [1., 0., 1., 0., 1., 0., 1., 0.]])
'''
new_list = [ x + 2 for x in range(0, 11)]
new_list
'''
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
'''
np_arr = np.array(range(0, 11))
np_arr + 2 # array([ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# We use linear equation for quantities which have linear relationship. Let's see the example below:

temp = np.array([1,2,3,4,5])
pressure = temp * 2 + 5
pressure
# array([ 7, 9, 11, 13, 15])

plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()

# To draw the Gaussian normal distribution using numpy. As you can see below, the numpy can generate random numbers. To create random sample, we need the mean(mu), sigma(standard deviation), mumber of data points.

mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()




