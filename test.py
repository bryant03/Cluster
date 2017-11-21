import numpy as np 


a=[[1,2,3],[4,5,6],[7,8,9]]

print(type(a))
b=np.array(a)
print(type(b),b.shape)
print(b[:,2])
print(b[:,:2])
c=[5,3,2,9]
c.sort()
print(c)
print(round(3.0))
belong=np.zeros(240)
print(belong)
for i in range(100,10):
    print(i)
