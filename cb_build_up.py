#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 19:40:47 2022

@author: damianesene
"""

import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import pandas as pd
import numpy as np
import pylab as pl
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Rectangle

cb_data = pd.read_excel('/Users/damianesene/Downloads/CB_BUILD_UP-3.xlsx')

a = cb_data['Prog Passes Per 90']
b= cb_data['Carries per 90']
c= cb_data['Player']
c = c.fillna("")



plt.rcParams.update({'font.family':'Rubik'})
bgcol = '#1d2849'

fig, ax= plt.subplots(figsize=(15,8),  dpi=120)

ax.scatter(a,b, color='#00a7e7')


for x,y,z in zip(a,b,c):
    label = "{}".format(z)
    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center', color='white')
    


fig.set_facecolor(bgcol)
ax.set_facecolor(bgcol)

plt.hlines(b.mean(), a.min(), a.max(), color='#c2c1c0')
plt.vlines(a.mean(), b.min(), b.max(), color='#c2c1c0')




# Change plot spines
ax.spines['right'].set_color('#ccc8c8')
ax.spines['top'].set_color('#ccc8c8')
ax.spines['left'].set_color('#ccc8c8')
ax.spines['bottom'].set_color('#ccc8c8')

fig.text(.15,.95,'How Center-Backs Contribute to Build-Up',size=20, color='white')
fig.text(.15,.92, 'Comparing top 10 progressive passing CBs in Europe top 5 leagues', size=12,color='white')
fig.text(.15,.89, 'Data gotten from FBREF', size=10, color='white')

fig.text(.80,.425,'Avg. Carries Per 90', size=6, color='white')
fig.text(.490,.13,'Avg. Prog. Passes Per 90', size=6, color='white',rotation=90)


fig.text(.490,.79,'Contributes with high number of foward passes and runs \n Laporte in a league of his own',size=10, color='white')
fig.text(.130,.79,'Contributes with high number of foward runs',size=10, color='white')
fig.text(.650,.19,'Contributes with high number of foward passes',size=10, color='white')

plt.ylabel('Carries Per 90',color='white')
plt.xlabel('Prog, Passes Per 90', color='white')


fig.savefig('/Users/damianesene/Downloads/cb_build_up.png', dpi=300)
