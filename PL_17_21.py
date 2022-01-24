#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 19:34:38 2022

@author: damianesene
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc #creates the patches
import json #reads json file
import matplotlib.patches as mpatches

from sklearn.linear_model import LinearRegression

df =pd.read_excel('/Users/damianesene/Downloads/PL_17_21-4.xlsx')




y = df['RK']
x= df['HomW%'].values.reshape(-1,1)

model=LinearRegression().fit(x,y)

r_sq = model.score(x,y)
intercept = model.intercept_
slope = model.coef_

y_pred = intercept + slope*x

plt.gca().invert_yaxis()
fig,ax = plt.subplots(figsize=(10,10))
plt.scatter(x,y)
plt.plot(x,y_pred, c='red')
plt.ylim(.5,20.5)
plt.yticks(np.arange(1, 21, 1))
plt.gca().invert_yaxis()


#fig.savefig('/Users/damianesene/Downloads/96_20_PL_rgsion.jpg', dpi=300)