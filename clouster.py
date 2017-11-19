import numpy as np
import matplotlib.pyplot as plt

def read_data(file_name):
    f=open(file_name)
    data=[]
    xx,yy=[],[]

    for i in f:
        i=i.split()
        data.append(i)
        xx.append(i[0])
        yy.append(i[1])
    data=np.asarray(data,dtype=np.float32)
    xx=np.asarray(xx,dtype=np.float32)
    yy=np.asarray(yy,dtype=np.float32)
    plt.plot(xx,yy,'o')
    plt.show()

    dis=np.zeros((240,240),dtype=np.float32)
    for  i in range(len(xx)):
        for j in range(len(yy)):
            dis[i,j]=(xx[i]-yy[j])*(xx[i]-yy[j])


if __name__ == '__main__':
    read_data('flame.txt')