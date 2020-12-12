from matplotlib import pyplot as plt
import scipy.io
from mat4py import loadmat
import glob
import os
import numpy as np
import pandas as pd

# Change the directory everytime to get xn
os.chdir('C:/Users/Eshika/Downloads/MLII/17 PR')

# Get a list for .mat files in current folder
mat_files = glob.glob('*.mat')

# List for stroring all the data
alldata = []

# Iterate mat files
for fname in mat_files:
    # Load mat file data into data.
    data = scipy.io.loadmat(fname)

    # Append data to the list
    alldata.append(data)
    
# for x1
x1=[]
for i in alldata:
    x1.append(i['val'])

x1 = np.array(x1)
x1 = pd.DataFrame(x1.reshape(283, -1))
x1['3600']=1

# for x2
x2=[]
for i in alldata:
    x2.append(i['val'])

x2 = np.array(x2)
x2 = pd.DataFrame(x2.reshape(66, -1))
x2['3600']=2

# for x3
x3=[]
for i in alldata:
    x3.append(i['val'])

x3 = np.array(x3)
x3 = pd.DataFrame(x3.reshape(20, -1))
x3['3600']=3

# for x4
x4=[]
for i in alldata:
    x4.append(i['val'])

x4 = np.array(x4)
x4 = pd.DataFrame(x4.reshape(135, -1))
x4['3600']=4

# for x5
x5=[]
for i in alldata:
    x5.append(i['val'])

x5 = np.array(x5)
x5 = pd.DataFrame(x5.reshape(13, -1))
x5['3600']=5

# for x6
x6=[]
for i in alldata:
    x6.append(i['val'])

x6 = np.array(x6)
x6 = pd.DataFrame(x6.reshape(21, -1))
x6['3600']=6

# for x7
x7=[]
for i in alldata:
    x7.append(i['val'])

x7 = np.array(x7)
x7 = pd.DataFrame(x7.reshape(133, -1))
x7['3600']=7

# for x8
x8=[]
for i in alldata:
    x8.append(i['val'])

x8 = np.array(x8)
x8 = pd.DataFrame(x8.reshape(55, -1))
x8['3600']=8

# for x9
x9=[]
for i in alldata:
    x9.append(i['val'])

x9 = np.array(x9)
x9 = pd.DataFrame(x9.reshape(13, -1))
x9['3600']=9

# for x10
x10=[]
for i in alldata:
    x10.append(i['val'])

x10 = np.array(x10)
x10 = pd.DataFrame(x10.reshape(10, -1))
x10['3600']=10

# for x11
x11=[]
for i in alldata:
    x11.append(i['val'])

x11 = np.array(x11)
x11 = pd.DataFrame(x11.reshape(10, -1))
x11['3600']=11

# for x12
x12=[]
for i in alldata:
    x12.append(i['val'])

x12 = np.array(x12)
x12 = pd.DataFrame(x12.reshape(10, -1))
x12['3600']=12

# for x13
x13=[]
for i in alldata:
    x13.append(i['val'])

x13 = np.array(x13)
x13 = pd.DataFrame(x13.reshape(11, -1))
x13['3600']=13

# for x14
x14=[]
for i in alldata:
    x14.append(i['val'])

x14 = np.array(x14)
x14 = pd.DataFrame(x14.reshape(103, -1))
x14['3600']=14

# for x15
x15=[]
for i in alldata:
    x15.append(i['val'])

x15 = np.array(x15)
x15 = pd.DataFrame(x15.reshape(62, -1))
x15['3600']=15

# for x16
x16=[]
for i in alldata:
    x16.append(i['val'])

x16 = np.array(x16)
x16 = pd.DataFrame(x16.reshape(10, -1))
x16['3600']=16

# for x16
x17=[]
for i in alldata:
    x17.append(i['val'])

x17 = np.array(x17)
x17 = pd.DataFrame(x17.reshape(45, -1))
x17['3600']=17

df = pd.concat([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17])
df = df.reset_index()
df = df.drop(['index'],axis=1)
df.to_csv('data.csv',index=False)
