import numpy as np
import matplotlib.pyplot as plt
import math

# -*- coding: UTF-8 -*-
class Cluster(object):
    """docstring for Cluster"""
    def __init__(self,file_name,size,percent):
        self.file_name=file_name
        self.size=size
        self.percent=percent
    def dis(self,a,b):
        return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)


 #  确定 dc  
    def cal_dc(self):
        position=round(len(self.dis_list)*(100-self.percent)/100)
        self.dis_list.sort()
        print('position is ',  position)
        return self.dis_list[position]

        
    def read_data(self):
        f=open(self.file_name)
        data=[]
        id= 0
        for i in f:
            i=i.split()
            i.append(123)
            i.append(id)
            for j in range(len(i)):
                i[j]=float(i[j])
            id+=1
            data.append(i)
        self.dis_list=[]
        d=np.asarray(data)
        plt.plot(d[:,0],d[:,1],'bo')
        plt.savefig(self.file_name+'.png')
        plt.show()
        # print(data)
        # 确定距离截断点


        for i in range(self.size):
            for j in range(i+1,self.size):
                self.dis_list.append(self.dis(data[i],data[j]))
        dc=self.cal_dc()
        print('dc is ',dc)
        # 计算密度
        for i in range(self.size):
            sum=0
            for j in range(i+1,self.size):        
                if self.dis(data[i],data[j])< 0.5:
                    sum+=1
            data[i].append(sum)

        data=sorted(data, key=lambda x:x[4])
        print(data)
        maxx=.0
        maxx_id=0
        # 计算相对距离
        for i in range(self.size-1):
            tmp=10000000.0
            tmp_id=0
            for j in range(i+1,self.size):
                if tmp>self.dis(data[i],data[j]):
                    tmp=self.dis(data[i],data[j])
                    tmp_id=data[j][3]
            data[i].append(round(tmp,2))
            data[i].append(tmp_id)
            if round(tmp,2)>maxx:
                maxx=round(tmp,2)
                maxx_id=data[i][3]
        # 计算密度最大点的相对距离
        data[self.size-1].append(maxx)
        data[self.size-1].append(maxx_id)

        da=np.array(data)
        print(da[:,5])
        plt.xlabel("dis")
        plt.ylabel("rho")
        plt.plot(da[:,4],da[:,5],'ro')
        # plt.plot(da[100:,4],da[100:,5],'o')
        plt.show()
        # for i in range(self.size):
        #     print(data[i])
        belong=np.zeros(self.size)
        print(data)
        print('寻找数据中心：')
        # 用来确定密度最大的点的归属，因为很有可能密度最大的点不是聚类中心
        tmp_dis=100000.
        clas=1
        for i in range(self.size):
            if data[i][4]>0 and data[i][5]>0.6:
                print(data[i])
                belong[round(data[i][3])]=clas
                if self.dis(data[i],data[self.size-1])<tmp_dis:
                    belong[round(data[self.size-1][3])]=clas
                    tmp_dis=self.dis(data[i],data[self.size-1])
                clas+=1
        print(belong)
        # 确认所有其他点的归属
        for i in range(self.size-1,-1,-1):
            if(belong[round(data[i][3])] == 0 ):
                belong[round(data[i][3])] = belong[round(data[i][6])]

        cnt1,cnt2=0,0
        print(belong)
        for i in belong:
            if i == 1:
                cnt1+=1
            elif i==2:
                cnt2+=1
            else:
                pass
        print('cnt1 is ',cnt1,'cnt2 is ',cnt2)
        col1=[]
        col2=[]
        col3=[]
        correct=0
        for i in data:
            if belong[round(i[3])] == 1 :
                col1.append(i[:2])
            elif belong[round(i[3])] == 2 :
                col2.append(i[:2])
            else:
                col3.append(i[:2])
            if belong[round(i[3])] == round(i[2]):
                correct+=1

        print('correct is ',correct)
        print('rate is ',correct/self.size)

        col1=np.asarray(col1)
        col2=np.asarray(col2)
        col3=np.asarray(col3)
        plt.plot(col1[:,0],col1[:,1],'bo')
        plt.plot(col2[:,0],col2[:,1],'ro')
        plt.plot(col3[:,0],col3[:,1],'yo')
        plt.savefig(self.file_name+"2.png")
        plt.show()

if __name__ == '__main__':
    cluster1=Cluster('ds6.ds',1500,2)
    cluster1.read_data()

    # cluster1=Cluster('spiral.txt',312,2)
    # cluster1.read_data()