#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 01:04:56 2021

@author: damianesene
"""

import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import pandas as pd
import numpy as np
import pylab as pl
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib as mpl

passdata = pd.read_excel('/Users/damianesene/Downloads/pass_types-2.xlsx')
a = passdata['High']
b = passdata['Ground']
#passdata['path'] = passdata['Squad'] + '.png'

# Set font and background colour
plt.rcParams.update({'font.family':'Avenir'})
bgcol = '#2B547E'

mpl.rcParams['text.color'] = 'white'

fig, ax = plt.subplots(figsize=(6, 4), dpi=120)

fig.set_facecolor(bgcol)
ax.set_facecolor(bgcol)
ax.scatter(a, b, c=bgcol)

def getImage(Path):
    return OffsetImage(plt.imread(Path), zoom=.05, alpha = 1)




for index, row in passdata.iterrows():
    ab = AnnotationBbox(getImage(row['Path']), (row['High'], row['Ground']), frameon=False)
    ax.add_artist(ab)

fig.text(.15,.95,'Club Pass Types',size=20)
fig.text(.15,.90,'How are PL teams passing this season?', size=12)
fig.text(.22,.70,'Keeps the ball \n on the ground',size=9)
fig.text(.62,.70,'Looks to mix things up',size=9)
fig.text(.15,.30,'Not passing enough',size=9)
fig.text(.62,.37,'Route one football',size=9)

plt.hlines(b.mean(), a.min(), a.max(), color='#c2c1c0')
plt.vlines(a.mean(), b.min(), b.max(), color='#c2c1c0')

## Avg line explanation
plt.ylabel('Ground Passes')
plt.xlabel('High Passes')

fig.text(.73,.460,'Avg. Ground Passes', size=8, color='#c2c1c0')
fig.text(.395,.17,'Avg. High Passes', size=8, color='#c2c1c0',rotation=90)

plt.savefig('pass_types.jpg', dpi=1200, bbox_inches = "tight")
