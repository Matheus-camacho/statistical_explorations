
# coding: utf-8

# In[141]:


import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random


# In[429]:


numBuses=10000000
buses=[0]*numBuses*5
for i in range(numBuses):
    num=random.randint(0,numBuses*5-1)
    while(buses[num]!=0):
        num=random.randint(0,numBuses*5-1)
    buses[num]=1
numSallys=10000
busesAfter=busesBefore=[]
differences=[]
for i in range(numSallys):
    count=0
    temp=sally=random.randint(0,numBuses*5-1)
    while(buses[temp]!=1):
        temp+=1
        count+=1
    busesAfter.append(count+1)
    diff=count+1
    count=0
    temp=sally
    while(buses[temp]!=1):
        temp-=1
        count+=1
    busesBefore.append(count+1)
    diff=diff+count+1
    differences.append(diff) 

dists=[]
last=0
for i in range(numBuses*5):
    if buses[i]==1:
        dists.append(i-last)
        last=i


# In[436]:


plt.xlabel("Wait time")
plt.ylabel("# of buses")
plt.hist(busesAfter, bins=100)
print("Average distance between buses:"+str(np.mean(dists)))
print("Average time of wait for bus:"+ str(np.mean(busesAfter)))
print("Average time from last missed bus:"+ str(np.mean(busesBefore)))
print("Average time between missed and next buses:"+str(np.mean(differences)))

