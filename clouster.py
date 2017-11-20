import numpy as np
import matplotlib.pyplot as plt
import math

class Cluster(object):
    """docstring for Cluster"""
    def __init__(self,file_name,size):
        self.file_name=file_name
        self.size=size
    def dis(self,a,b):
        return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

    def read_data(self):
        f=open(self.file_name)
        data=[]
        id= 0
        for i in f:
            i=i.split()
            i.append(id)
            for j in range(len(i)):
                i[j]=float(i[j])
            id+=1
            data.append(i)
        # data=np.asarray(data,dtype=np.float32)
        # xx=np.asarray(xx,dtype=np.float32)
        # yy=np.asarray(yy,dtype=np.float32)
        # plt.plot(xx,yy,'o')
        # plt.show()
        # dis=np.zeros((240,240),dtype=np.float32)
        # for  i in range(len(xx)):
        #     for j in range(i,len(yy)):
        #         dis[i,j]=(xx[i]-yy[j])*(xx[i]-yy[j])
        # dis=np.sqrt(dis)
        dc=4.0
        for i in range(self.size):
            sum=0
            for j in range(self.size):
                if i!=j:
                    if self.dis(data[i],data[j])< dc:
                        # print(self.dis(data[i],data[j]))
                        sum+=1
            data[i].append(sum)
        # print(data)
        print (sorted(data, key=lambda x:x[4]))
        # print (data[:][3])
        for i in range(239):
            tmp=.0
            for j in range(i,239):
                if tmp<dis[]



if __name__ == '__main__':
    cluster=Cluster('flame.txt',240)
    cluster.read_data()
