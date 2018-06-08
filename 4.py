import numpy as np
x=np.array([[0,1],[2,3]])
y=np.array([[4,5],[6,7]])

v=np.array([8,9])
w=np.array([10,11])
print(v.dot(w))
print(np.dot(v,w))
 
print(x.dot(v))
print(np.dot(x,v))

print(x.dot(y))
print(np.dot(x,y))

x=np.array([[1,2],[3,4]])
print(np.sum(x))
print(np.sum(x, axis=0))
print(np.sum(x, axis=1))
x=np.array([[1,2],[3,4]])
print(x)
print(x.T)
