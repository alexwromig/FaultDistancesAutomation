#!/usr/bin/env python
# coding: utf-8

# # Automatic Kilometer to Mile Conversion for Fault Distances

# # 1: Import Modules

# In[1]:


import numpy as np
import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog


# # 2: Choose Fault Distances File

# In[2]:


# Create Tk root
root = tk.Tk()

# Hide the main window
root.withdraw()
root.call('wm', 'attributes', '.', '-topmost', True)

# select file dialog
file_path = filedialog.askopenfilename()

#get_ipython().run_line_magic('gui', 'tk')


# # 3: Add Mile Column to Table

# In[40]:


conv = 0.621371 # km to mi conversion

# read text file, format it for pandas (names are abbreviated column names)
FD = pd.read_csv(file_path, sep='|', skiprows = 71, names = ['FAULT','KM',
                                                             'SOURCE','Mw','SLIP',
                                                             'TYPE'])

# Add mile conversion column
FD['MI'] = FD['KM']*conv

# limit to 2 decimal places
FD['MI'] = FD['MI'].round(2)

# reorganize columns
FD = FD[['FAULT','MI','KM','SOURCE',
         'Mw','SLIP','TYPE']]


# # 4: Print Table and Replace in Text File

# In[43]:


print(FD.to_string(header=True, index=False, col_space = [32,5,8,7,4,7,10], justify='center'))


# # Questions to ask:
# # 1. Headers need to be the same?
# # 2. fit within dimensions of original text file?

# In[ ]:




