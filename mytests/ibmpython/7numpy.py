import numpy as np

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
print(a)

# Convert list to Numpy Array
A = np.array(a)
print(A)
print("ndim:", A.ndim)
print("Shape: ", A.shape)
print("Size: ", A.size)
print("A 1,2 is:",A[1,2])
print("Same stuff, A 1,2 is:",A[1][2])
print("Slicing: ", A[0][0:2])
print("Slicing row: ", A[0:2,2])


X = np.array([[1, 4], [3, 1]]) 
Y = np.array([[2, 1], [1, 2]]) 
print(X)
print(Y)
Z = X + Y
print(Z)

Y2 = Z * 2
print(Y2)

MULY = X * Y 
print(MULY)

V = np.array([[0, 1, 1], [1, 0, 1]])
B = np.array([[1, 1], [1, 1], [-1, 1]])
VB = np.dot(V,B)
print("VB: ",VB)
print(np.sin(VB))

C = np.array([[1,1],[2,2],[3,3]])
print("C.T is:", C.T)

print("V is:",V[1])
print("A is:", A[:, 2])

Q = np.array([2, 5])
W = np.array([5, 3])
QW = np.dot(Q,W)
print("QW: ",QW)

print(type(a))
print(type(A))

X=np.array([[1,0,1],[2,2,2]]) 
out=X[0:2,2]
print(out)

X=np.array([[1,0],[0,1]]) 
Y=np.array([[2,1],[1,2]]) 
Z=np.dot(X,Y) 
print("z again:",Z)
