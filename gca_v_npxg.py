#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 00:47:50 2023

@author: damianesene
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup, Comment
import numpy as np
import pylab as pl
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.patches as patches
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)
import matplotlib.image as image

prem_url = 'https://fbref.com/en/comps/9/shooting/Premier-League-Stats#stats_shooting::21'


response = requests.get(prem_url)

tables = pd.read_html(response.text, header=1)

# Get the tables within the Comments
soup = BeautifulSoup(response.text, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for each in comments:
    if 'table' in str(each):
        try:
            epl_tbl = pd.read_html(str(each), header=1)[0]
            epl_tbl = epl_tbl[epl_tbl['Rk'].ne('Rk')].reset_index(drop=True)
            epl_tbl.append(epl_tbl)
        except:
            continue
        
epl_tbl["90s"] = pd.to_numeric(epl_tbl["90s"])
#epl_tbl["Age"] = pd.to_numeric(epl_tbl["Age"])
epl_tbl["SoT/90"] = pd.to_numeric(epl_tbl["SoT/90"])
epl_tbl["npxG"] = pd.to_numeric(epl_tbl["npxG"])
#epl_tbl["G/Shp90"] = epl_tbl["G/Sh"]/epl_tbl["90s"]
epl_tbl["npxG/90"] = epl_tbl["npxG"]/epl_tbl["90s"]

epl_tbl = epl_tbl[epl_tbl["90s"] >=9]

epl_tbl=epl_tbl[(epl_tbl["Pos"]=="FW,MF") | (epl_tbl["Pos"]=="FW") | (epl_tbl["Pos"]=="MF,FW")]

###################################################################################################
gca_url = 'https://fbref.com/en/comps/9/gca/Premier-League-Stats#stats_gca::17'
response = requests.get(gca_url)

tables = pd.read_html(response.text, header=1)

# Get the tables within the Comments
soup = BeautifulSoup(response.text, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for each in comments:
    if 'table' in str(each):
        try:
            gca_tbl = pd.read_html(str(each), header=1)[0]
            gca_tbl = gca_tbl[gca_tbl['Rk'].ne('Rk')].reset_index(drop=True)
            gca_tbl.append(gca_tbl)
        except:
            continue
        

gca_tbl["90s"] = pd.to_numeric(gca_tbl["90s"])
gca_tbl = gca_tbl[gca_tbl["90s"] >=9]
gca_tbl=gca_tbl[(gca_tbl["Pos"]=="FW,MF") | (gca_tbl["Pos"]=="FW") | (gca_tbl["Pos"]=="MF,FW")]
gca_tbl["GCA90"] = pd.to_numeric(gca_tbl["GCA90"])

epl_tbl["GCA90"]= gca_tbl["GCA90"]
epl_tbl = epl_tbl.sort_values(by=['Squad'])
epl_tbl = epl_tbl.reset_index(drop=True)
epl_tbl["Color"] = ''
epl_tbl.loc[0:2,['Color']] = ['red']
epl_tbl.loc[3:6,['Color']] = ['maroon']
epl_tbl.loc[7:11,['Color']] = ['black']
epl_tbl.loc[12:14,['Color']] = ['red']
epl_tbl.loc[15:16,['Color']] = ['cyan']
epl_tbl.loc[17:20,['Color']] = ['blue']
epl_tbl.loc[21:25,['Color']] = ['purple']
epl_tbl.loc[26:27,['Color']] = ['#29465B']
epl_tbl.loc[28:29,['Color']] = ['white']
epl_tbl.loc[30:32,['Color']] = ['Yellow']
epl_tbl.loc[33:35,['Color']] = ['blue']
epl_tbl.loc[36:39,['Color']] = ['#F62817']
epl_tbl.loc[40:43,['Color']] = ['#43C6DB']
epl_tbl.loc[44:46,['Color']] = ['#FD1C03']
epl_tbl.loc[47:49,['Color']] = ['#565051']
epl_tbl.loc[50:52,['Color']] = ['red']
epl_tbl.loc[53:56,['Color']] = ['#CB6D51']
epl_tbl.loc[57:59,['Color']] = ['#123456']
epl_tbl.loc[60:64,['Color']] = ['#560319']
epl_tbl.loc[65:66,['Color']] = ['#F87217']

epl_tbl.loc[1,['Player']] = ['']
epl_tbl.loc[4:5,['Player']] = ['']
epl_tbl.loc[7:11,['Player']] = ['']
epl_tbl.loc[12,['Player']] = ['']
epl_tbl.loc[14:16,['Player']] = ['']
epl_tbl.loc[17:19,['Player']] = ['']
epl_tbl.loc[20,['Player']] = ['']
epl_tbl.loc[21:22,['Player']] = ['']
epl_tbl.loc[23:28,['Player']] = ['']
epl_tbl.loc[33:34,['Player']] = ['']
epl_tbl.loc[36,['Player']] = ['']
epl_tbl.loc[39,['Player']] = ['']
epl_tbl.loc[43,['Player']] = ['']
epl_tbl.loc[47:49,['Player']] = ['']
epl_tbl.loc[30:32,['Player']] = ['']
epl_tbl.loc[50:55,['Player']] = ['']
epl_tbl.loc[59,['Player']] = ['']
epl_tbl.loc[60:61,['Player']] = ['']
#epl_tbl.loc[62:64,['Player']] = ['']
epl_tbl.loc[65:66,['Player']] = ['']



        

a = epl_tbl['npxG/90']
b = epl_tbl['GCA90']
d= epl_tbl['Player']
e = epl_tbl['Color']
plt.rcParams.update({'font.family':'sans-serif'})
bgcol = '#2B547E'

#mpl.rcParams['text.color'] = 'white'

fig, ax = plt.subplots(figsize=(19, 10), dpi=120)
ax.scatter(a,b, c = e, alpha=0.8)
fig.set_facecolor(bgcol)
ax.set_facecolor(bgcol)
#ax.scatter(a, b, color='#ffa500')

fig= plt.figure(1, figsize=(19, 10), frameon=False, dpi=100)
for x,y,z in zip(a,b,d):
    label = "{}".format(z)
    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center')
plt.ylabel('Goal Creating Action/90',color='white',size=15)
plt.xlabel('Non-Penalty xG/90',color='white',size=15)
#plt.grid(linestyle = '--', alpha=0.3)

plt.hlines(epl_tbl['GCA90'].mean(), epl_tbl['npxG/90'].min(), epl_tbl['npxG/90'].max(), color='#c2c1c0')
plt.vlines(epl_tbl['npxG/90'].mean(), epl_tbl['GCA90'].min(), epl_tbl['GCA90'].max(), color='#c2c1c0')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#ccc8c8')
ax.spines['bottom'].set_color('#ccc8c8')


############### ADD LOGO ######################################
# =============================================================================
# file = "/Users/damianesene/Downloads/my_logo.jpg"
# logo = image.imread(file)
# imagebox = OffsetImage(logo, zoom = 0.08)
# ab = AnnotationBbox(imagebox, (0.2, 1.1), frameon = False)
# ax.add_artist(ab)
# 
# =============================================================================

rect=patches.Rectangle((0.4, 0.8), 0.23, 0.2,facecolor='none',edgecolor='r')
rect1=patches.Rectangle((0.47, 0.12), 0.21, 0.2,facecolor='none',edgecolor='r')
ax.add_patch(rect)
ax.add_patch(rect1)
plt.text(0.41,0.87,"Gets in good positions to score\nCreates goal scoring opp for teammates", size=15)
plt.text(0.48,0.19,"Gets in good positions to score\nDoesn't create much for teammates", size=15)
plt.text(0.3,1.5,"Goal Scoring v Goal Creation", size=25)
plt.text(0.31,1.43,"Analyzing Premier League attackers",size = 18, color = "#34282C")
plt.text(0.28,1.38,"Data as of 07/02/23 || Data gotten from Fbref || @dame_world",size = 15, color = "#34282C")
#plt.text(2,35,'Comparing Forwards in the T5 leagues \n based on Pressures made and pressures made in attacking 3rd per 90', size=9.5, color='white')

fig.savefig('/Users/damianesene/Downloads/gca_v_npxg.jpg', dpi=300, bbox_inches='tight')