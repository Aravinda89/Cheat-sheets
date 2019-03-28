import numpy as np

# Creating Arrays
a = np.array([1, 2, 3])
b = np.array([(1.5, 2, 3), (4, 5, 6)])
b = np.array([[1.5, 2, 3], [4, 5, 6]])
c = np.array([[(1.5, 2, 3), (4, 5, 6)], [(3, 2, 1), (4, 5, 6)]], dtype=float)

# Placeholders
zeros = np.zeros((2, 2))
ones = np.ones((2, 2))
d = np.arange(0, 51, 5)
np.linspace(0, 21, 3)

np.full((3,3),5)
np.eye(3)
np.random.random((5,5))
np.empty((2,2))

# Inspecting arrays
a.shape
len(a)
b.ndim
c.ndim
c.size
b.size
b.dtype
b.dtype.name
b.astype(int)

# Array Mathmatics
a-b
np.subtract(a,b)
a+b
np.add(a,b)
a/b
np.divide(a,b)
a*b
np.multiply(a,b)
np.exp(b)
np.sqrt(b)
np.sin(b)
np.cos(b)
np.log(b)
a.dot(b.T)

# Comparison
a == b
a < 3
np.array_equal(a, a.copy())

# Aggregate function
a.sum()
a.min()
b.max(axis=0)
b.cumsum(axis=0)
a.mean()
np.std(b)

# Copy arrays
h = a.view()
np.copy(a)
g = a.copy()

# Sorting
a.sort()
b.sort(axis=0)

# Subsetting
a[2]
b[0, 1]

# Slicing
a[0: 2]
b[:, 1]
b[: 1]

c[1, :, :]
c[1, ...]

a[: :-1] # Reverse array

# Boolean Indexing
b[b > 4]

b[[0, 1, 1],[0, 1, 2]]
b[[1, 0]][:, [2]]

# Manipulation
np.transpose(b)
b.T

b.ravel()
b.reshape(3, -1)
b.resize(3, 2)
np.append(a, -2)
np.insert(a, 1, 20)
np.delete(a, [1])

# Combining
j = np.array([[3, 3]])
np.concatenate((b, j), axis=0)

k = np.array([0, 0])
np.vstack((k, b))

l = np.array([1, 1])

np.r_[k, l]
np.hstack((k, l))
np.column_stack((k, l))
np.c_[k, l]

# Splitting
np.hsplit(a, 2)
np.vsplit(b, 3)




