#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import seaborn as sns


# In[3]:


from matplotlib import pyplot as plt


# In[9]:


ipl= pd.read_csv('ipl.csv')


# In[11]:


ipl.head()


# In[12]:


ipl.tail()


# In[13]:


ipl.shape


# In[14]:


ipl.describe()


# In[16]:


#check the frequency of mom by value counts fxn
ipl['player_of_match'].value_counts()


# In[19]:


ipl['player_of_match'].value_counts()[0:10]


# In[21]:


ipl['player_of_match'].value_counts()[0:5]


# In[22]:


#bar plot
list(ipl['player_of_match'].value_counts()[0:5].keys())


# In[34]:


plt.figure(figsize=(9,5))
plt.bar(list(ipl['player_of_match'].value_counts()[0:5].keys()),list(ipl['player_of_match'].value_counts()[0:5]),color="r")

plt.show()


# In[36]:


ipl['result'].value_counts()


# In[37]:


list(ipl['result'].value_counts().keys())


# In[44]:


plt.figure(figsize=(7,4))
plt.bar(list(ipl['result'].value_counts().keys()),list(ipl['result'].value_counts()))
plt.show()


# In[45]:


ipl['toss_winner'].value_counts()


# In[53]:


#check batting first team wins

batting_first=ipl[ipl['win_by_runs']!=0]


# In[58]:


batting_first.head()


# In[64]:


#histogram plot for margin of runs
plt.figure(figsize=(5,5))
plt.hist(batting_first['win_by_runs'],color="r")
plt.title('distribution of runs')
plt.xlabel('runs')
plt.ylabel('matches')
plt.show()


# In[65]:


batting_first['winner'].value_counts()


# In[66]:


#bar plot  for top 5 teams
list(batting_first['winner'].value_counts()[0:6].keys())


# In[86]:


plt.figure(figsize=(15,7))
plt.bar(list(batting_first['winner'].value_counts()[0:6].keys()),list(batting_first['winner'].value_counts()[0:6]),color=['yellow','blue','red','purple','green','pink'])
plt.show()


# In[90]:


#pie chart
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%',radius=3)
plt.show()


# In[ ]:





# In[96]:


batting_second=ipl[ipl['win_by_wickets']!=0]


# In[97]:


batting_second.head()


# In[99]:


plt.hist(batting_second['win_by_wickets'],color='r')
plt.title('distribution')
plt.xlabel('wickets')
plt.ylabel('matches')
plt.show()


# In[100]:


batting_second['winner'].value_counts()


# In[101]:


list(batting_second['winner'].value_counts()[0:4].keys())


# In[106]:


plt.figure(figsize=(10,4))
plt.bar(list(batting_second['winner'].value_counts()[0:4].keys()),list(batting_second['winner'].value_counts()[0:4]),color=('red','purple','green','pink'))
plt.show()


# In[113]:


#pie chart
plt.pie(list(batting_second['winner'].value_counts()),labels=list(batting_second['winner'].value_counts().keys()),autopct='%0.1f%%',radius=3
    )
plt.show()


# In[114]:


ipl['city'].value_counts()


# In[115]:


ipl['season'].value_counts()


# In[116]:


#finding record that how many teams wins both toss and match
import numpy as np
np.sum(ipl['toss_winner']==ipl['winner'])


# In[117]:


291/576


# In[118]:


deliveries=pd.read_csv('deliveries.csv')


# In[119]:


deliveries.head()


# In[121]:


deliveries['match_id'].unique()


# In[122]:


match_1=deliveries[deliveries['match_id']==1]


# In[123]:


match_1.head()


# In[124]:


match_1.shape


# In[127]:


srh=match_1[match_1['inning']==1]


# In[128]:


srh['batsman_runs'].value_counts()


# In[129]:


srh['dismissal_kind'].value_counts()


# In[130]:


rcb=match_1[match_1['inning']==2]


# In[132]:


rcb['batsman_runs'].value_counts()


# In[133]:


rcb['dismissal_kind'].value_counts()


# In[135]:


rcb['extra_runs'].value_counts()


# In[ ]:




