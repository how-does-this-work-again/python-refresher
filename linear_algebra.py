import numpy as np

# problem 1
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
p1a = a + b
p1b = a - b
print("p1a:", p1a, "\np1b:", p1b)

# problem 2
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
p2a = A + B
p2b = A - B
print("p2a:", p2a, "\np2b:", p2b)

# problem 3
p3 = np.dot(a, b)
print("p3:",p3)

# problem 4
C = np.array([[1, 2, 3], [4, 5, 6]])
D = np.array([[7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18]])
p4 = np.dot(C, D)
print("p4:",p4)

# problem 5
c = np.array([1, 1, 2])
p5 = np.linalg.norm(c)
print("p5:",p5)

# problem 6
p6 = A.T
print("p6:",p6)
