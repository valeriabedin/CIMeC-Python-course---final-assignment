#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

import pandas as pd

import numpy as np 

import matplotlib.pyplot as plt


import scipy

import re



# In[2]:


left_sound_trace=pd.read_csv("interleaved_data.txt", names=["Left Ear"])
left_sound_trace


# In[3]:


#plot the sound trace recorded over time
#left_sound_trace.plot()
#left_sound_trace.axhline(100)
threshold=100

fig, axes= plt.subplots(figsize=(9,3))

axes.plot(left_sound_trace)

axes.axhline(threshold, color='red', linestyle='--')

axes.set_xlabel('Time')

fig.show()


# In[ ]:




