
#%%
import os
import pandas
# import numpy
from pandas import DataFrame,Series
def openfile(numpylist):
    path=os.getcwd()+r'\dataanalysis\label'
    filenamelist=list()
    for root,dirs,files in os.walk(path):
        for file in files:
            filenamelist.append(os.path.join(root,file))
    num=0
    for i in filenamelist:
        with open(i) as fp:
            numpylist.append(pandas.read_csv(i,names=['data']))
        num+=1
def openfile1(numpylist):
    path=os.getcwd()+r'\dataanalysis\train'
    filenamelist=list()
    for root,dirs,files in os.walk(path):
        for file in files:
            filenamelist.append(os.path.join(root,file))
    num=0
    for i in filenamelist:
        with open(i) as fp:
            numpylist.append(pandas.read_csv(i,index_col=None,header=None))
        num+=1
    
def openfile2(numpylist):
    path=os.getcwd()+r'\dataanalysis\test'
    filenamelist=list()
    for root,dirs,files in os.walk(path):
        for file in files:
            filenamelist.append(os.path.join(root,file))
    num=0
    for i in filenamelist:
        with open(i) as fp:
            numpylist.append(pandas.read_csv(i,index_col=None,header=None))
        num+=1

def sort_and_record(goal_numpy):
    goal_numpy['oldseq']=list(goal_numpy.index)
    for index,row in goal_numpy.iterrows():
        row['data']=abs(row['data'])
    goal_numpy.sort_values('data',ascending=False,inplace=True)


numpylist=list()
numpylist1=list()
numpylist2=list()
openfile(numpylist)
CEMTL_Male=numpylist[0]
CEMTL_White=numpylist[1]
CMTL_Male=numpylist[2]
CMTL_White=numpylist[3]
MTL_Male=numpylist[4]
MTL_White=numpylist[5]
sort_and_record(CMTL_Male)
# print(CMTL_Male)
sort200=CMTL_Male.head(200)
# openfile1(numpylist1)
# TrainSample=numpylist1[0]

# # print(sort200)
# TrainSub=DataFrame()
# num=0
# for index,row in sort200.iterrows():
#     a=row['oldseq']
#     # print(a)
#     TrainSub[num]=TrainSample[a]
#     num+=1
# # print(TrainSub)

openfile2(numpylist2)
TestSample=numpylist2[0]
print(TestSample)
# print(sort200)
TestSub=DataFrame()
num=0
for index,row in sort200.iterrows():
    a=row['oldseq']
    # print(a)
    TestSub[num]=TestSample[a]
    num+=1
print(TestSub)


# MTL_White_train=numpylist1[1]
# print(TrainSample)
