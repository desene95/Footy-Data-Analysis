#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 23:29:03 2022

@author: damianesene
"""

import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import pandas as pd
import numpy as np
import pylab as pl
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

pl_fwds=pd.read_excel('/Users/damianesene/Downloads/PL_FWDS-8.xlsx')

a= pl_fwds['GCA90']
b= pl_fwds['xG'] 
c= pl_fwds['Player']
c= c.fillna("")
d=pl_fwds['Color']


plt.rcParams.update({'font.family':'Avenir'})
bgcol = '#2B547E'

fig, ax = plt.subplots(figsize=(6, 4), dpi=120)
ax.scatter(a, b, color = d, alpha=0.5)
fig.set_facecolor(bgcol)
ax.set_facecolor(bgcol)

#fig= plt.figure(1, figsize=(8, 15), frameon=False, dpi=100)
for x,y,z in zip(a,b,c):
    label = "{}".format(z)
    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center')


plt.ylabel('XG',color='white')
plt.xlabel('Goal creating action/90',color='white')

plt.hlines(pl_fwds['xG'].mean(), pl_fwds['GCA90'].min(), pl_fwds['GCA90'].max(), color='#c2c1c0')
plt.vlines(pl_fwds['GCA90'].mean(), pl_fwds['xG'].min(), pl_fwds['xG'].max(), color='#c2c1c0')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#ccc8c8')
ax.spines['bottom'].set_color('#ccc8c8')
plt.text(-0.1,27,'Analyzing Fowards and midfielders\nWho is finding himself in good goal scoring\n positions and also creating goal scoring chances for teammates', size=12, color='white')
plt.text(-0.1,25.6,'* Salah in a world of his own', size=10, color='white')
plt.text(-0.1,24.3,'* Gabriel Jesus showing why he is what Arsenal are missing', size=10, color='white')
plt.text(-0.1,23.2,'* Harry Kane, the "Modern Day No 9"', size=10, color='white')
plt.text(0.7,-4,'Data gotten from fbref', size=5, color='white')
plt.text(0,-4,'Twitter: @dame_world', size=5, color='white')
plt.grid(linestyle = '--', alpha=0.3)

plt.show()