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
