#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 31 23:54:06 2022

@author: damianesene
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup, Comment
import numpy as np
import pylab as pl
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt

prem_shot_url = 'https://fbref.com/en/comps/9/shooting/Premier-League-Stats#stats_shooting'
response = requests.get(prem_shot_url)

tables = pd.read_html(response.text, header=1)

# Get the tables within the Comments
soup = BeautifulSoup(response.text, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for each in comments:
    if 'table' in str(each):
        try:
            epl_shot = pd.read_html(str(each), header=1)[0]
            epl_shot = epl_shot[epl_shot['Rk'].ne('Rk')].reset_index(drop=True)
            epl_shot.append(epl_shot)
        except:
            continue
        
epl_shot["90s"] = pd.to_numeric(epl_shot["90s"])
epl_shot["Age"] = pd.to_numeric(epl_shot["Age"])
epl_shot["xG"] = pd.to_numeric(epl_shot["xG"])
epl_shot["npxG"] = pd.to_numeric(epl_shot["npxG"])
epl_shot["xG/90"] = epl_shot["xG"]/epl_shot["90s"]
epl_shot["npxG/90"] = epl_shot["npxG"]/epl_shot["90s"]
#epl_shot["Age"]=epl_shot["Age"]<=30
epl_shot = epl_shot[epl_shot["Age"] <=30]
epl_shot = epl_shot[epl_shot["90s"] >=15]
#epl_shot=epl_shot["90s"]>=15
epl_shot=epl_shot[(epl_shot["Pos"]=="FW,MF") | (epl_shot["Pos"]=="FW") | (epl_shot["Pos"]=="MF,FW")]


prem_gca_url = 'https://fbref.com/en/comps/9/gca/Premier-League-Stats#stats_gca'
response = requests.get(prem_gca_url)

tables = pd.read_html(response.text, header=1)

# Get the tables within the Comments
soup = BeautifulSoup(response.text, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for each in comments:
    if 'table' in str(each):
        try:
            prem_gca = pd.read_html(str(each), header=1)[0]
            prem_gca = prem_gca[prem_gca['Rk'].ne('Rk')].reset_index(drop=True)
            prem_gca.append(prem_gca)
        except:
            continue
        
prem_gca["90s"] = pd.to_numeric(prem_gca["90s"])
prem_gca["Age"] = pd.to_numeric(prem_gca["Age"])
prem_gca["SCA"] = pd.to_numeric(prem_gca["SCA"])
prem_gca["GCA"] = pd.to_numeric(prem_gca["GCA"])
prem_gca["SCA90"] = pd.to_numeric(prem_gca["SCA90"])
prem_gca["GCA90"] = pd.to_numeric(prem_gca["GCA90"])
#epl_shot["xG/90"] = epl_shot["xG"]/epl_shot["90s"]
#epl_shot["npxG/90"] = epl_shot["npxG"]/epl_shot["90s"]
#epl_shot["Age"]=epl_shot["Age"]<=30
prem_gca = prem_gca[prem_gca["Age"] <=30]
prem_gca = prem_gca[prem_gca["90s"] >=15]
#epl_shot=epl_shot["90s"]>=15
prem_gca=prem_gca[(prem_gca["Pos"]=="FW,MF") | (prem_gca["Pos"]=="FW") | (prem_gca["Pos"]=="MF,FW")]
prem=pd.merge( prem_gca, epl_shot, on=["Rk","Player","Nation","Pos","Squad","Age","Born","90s","Matches"])

###############################################################################

laliga_shot_url = 'https://fbref.com/en/comps/12/shooting/La-Liga-Stats#stats_shooting'
response = requests.get(laliga_shot_url)

tables = pd.read_html(response.text, header=1)

# Get the tables within the Comments
soup = BeautifulSoup(response.text, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for each in comments:
    if 'table' in str(each):
        try:
            laliga_shot = pd.read_html(str(each), header=1)[0]
            laliga_shot = laliga_shot[laliga_shot['Rk'].ne('Rk')].reset_index(drop=True)
            laliga_shot.append(laliga_shot)
        except:
            continue
        
laliga_shot["90s"] = pd.to_numeric(laliga_shot["90s"])
laliga_shot["Age"] = pd.to_numeric(laliga_shot["Age"])
laliga_shot["xG"] = pd.to_numeric(laliga_shot["xG"])
laliga_shot["npxG"] = pd.to_numeric(laliga_shot["npxG"])
laliga_shot["xG/90"] = laliga_shot["xG"]/laliga_shot["90s"]
laliga_shot["npxG/90"] = laliga_shot["npxG"]/laliga_shot["90s"]
laliga_shot = laliga_shot[laliga_shot["Age"] <=30]
laliga_shot = laliga_shot[laliga_shot["90s"] >=15]
laliga_shot=laliga_shot[(laliga_shot["Pos"]=="FW,MF") | (laliga_shot["Pos"]=="FW") | (laliga_shot["Pos"]=="MF,FW")]



laliga_gca_url = 'https://fbref.com/en/comps/12/gca/La-Liga-Stats#stats_gca'
response = requests.get(laliga_gca_url)

tables = pd.read_html(response.text, header=1)

# Get the tables within the Comments
soup = BeautifulSoup(response.text, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for each in comments:
    if 'table' in str(each):
        try:
            laliga_gca = pd.read_html(str(each), header=1)[0]
            laliga_gca = laliga_gca[laliga_gca['Rk'].ne('Rk')].reset_index(drop=True)
            laliga_gca.append(laliga_gca)
        except:
            continue
        
laliga_gca["90s"] = pd.to_numeric(laliga_gca["90s"])
laliga_gca["Age"] = pd.to_numeric(laliga_gca["Age"])
laliga_gca["SCA"] = pd.to_numeric(laliga_gca["SCA"])
laliga_gca["GCA"] = pd.to_numeric(laliga_gca["GCA"])
laliga_gca["SCA90"] = pd.to_numeric(laliga_gca["SCA90"])
laliga_gca["GCA90"] = pd.to_numeric(laliga_gca["GCA90"])
#epl_shot["xG/90"] = epl_shot["xG"]/epl_shot["90s"]
#epl_shot["npxG/90"] = epl_shot["npxG"]/epl_shot["90s"]
#epl_shot["Age"]=epl_shot["Age"]<=30
laliga_gca = laliga_gca[laliga_gca["Age"] <=30]
laliga_gca = laliga_gca[laliga_gca["90s"] >=15]
#epl_shot=epl_shot["90s"]>=15
laliga_gca=laliga_gca[(laliga_gca["Pos"]=="FW,MF") | (laliga_gca["Pos"]=="FW") | (laliga_gca["Pos"]=="MF,FW")]
laliga= pd.merge( laliga_gca, laliga_shot, on=["Rk","Player","Nation","Pos","Squad","Age","Born","90s","Matches"])

###########################################################################################################################

seriea_shot_url = 'https://fbref.com/en/comps/11/shooting/Serie-A-Stats#stats_shooting'
response = requests.get(seriea_shot_url)

tables = pd.read_html(response.text, header=1)

# Get the tables within the Comments
soup = BeautifulSoup(response.text, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for each in comments:
    if 'table' in str(each):
        try:
            seriea_shot = pd.read_html(str(each), header=1)[0]
            seriea_shot = seriea_shot[seriea_shot['Rk'].ne('Rk')].reset_index(drop=True)
            seriea_shot.append(seriea_shot)
        except:
            continue
        
seriea_shot["90s"] = pd.to_numeric(seriea_shot["90s"])
seriea_shot["Age"] = pd.to_numeric(seriea_shot["Age"])
seriea_shot["xG"] = pd.to_numeric(seriea_shot["xG"])
seriea_shot["npxG"] = pd.to_numeric(seriea_shot["npxG"])
seriea_shot["xG/90"] = seriea_shot["xG"]/seriea_shot["90s"]
seriea_shot["npxG/90"] = seriea_shot["npxG"]/seriea_shot["90s"]
seriea_shot = seriea_shot[seriea_shot["Age"] <=30]
seriea_shot = seriea_shot[seriea_shot["90s"] >=15]
seriea_shot=seriea_shot[(seriea_shot["Pos"]=="FW,MF") | (seriea_shot["Pos"]=="FW") | (seriea_shot["Pos"]=="MF,FW")]



seriea_gca_url = 'https://fbref.com/en/comps/11/gca/Serie-A-Stats#stats_gca'
response = requests.get(seriea_gca_url)

tables = pd.read_html(response.text, header=1)

# Get the tables within the Comments
soup = BeautifulSoup(response.text, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for each in comments:
    if 'table' in str(each):
        try:
            seriea_gca = pd.read_html(str(each), header=1)[0]
            seriea_gca = seriea_gca[seriea_gca['Rk'].ne('Rk')].reset_index(drop=True)
            seriea_gca.append(seriea_gca)
        except:
            continue
        
seriea_gca["90s"] = pd.to_numeric(seriea_gca["90s"])
seriea_gca["Age"] = pd.to_numeric(seriea_gca["Age"])
seriea_gca["SCA"] = pd.to_numeric(seriea_gca["SCA"])
seriea_gca["GCA"] = pd.to_numeric(seriea_gca["GCA"])
seriea_gca["SCA90"] = pd.to_numeric(seriea_gca["SCA90"])
seriea_gca["GCA90"] = pd.to_numeric(seriea_gca["GCA90"])
#epl_shot["xG/90"] = epl_shot["xG"]/epl_shot["90s"]
#epl_shot["npxG/90"] = epl_shot["npxG"]/epl_shot["90s"]
#epl_shot["Age"]=epl_shot["Age"]<=30
seriea_gca = seriea_gca[seriea_gca["Age"] <=30]
seriea_gca = seriea_gca[seriea_gca["90s"] >=15]
#epl_shot=epl_shot["90s"]>=15
seriea_gca=seriea_gca[(seriea_gca["Pos"]=="FW,MF") | (seriea_gca["Pos"]=="FW") | (seriea_gca["Pos"]=="MF,FW")]
seriea= pd.merge( seriea_gca, seriea_shot, on=["Rk","Player","Nation","Pos","Squad","Age","Born","90s","Matches"])

#####################################################################################################################

bundes_shot_url = 'https://fbref.com/en/comps/20/shooting/Bundesliga-Stats#stats_shooting'
response = requests.get(bundes_shot_url)

tables = pd.read_html(response.text, header=1)

# Get the tables within the Comments
soup = BeautifulSoup(response.text, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for each in comments:
    if 'table' in str(each):
        try:
            bundes_shot = pd.read_html(str(each), header=1)[0]
            bundes_shot = bundes_shot[bundes_shot['Rk'].ne('Rk')].reset_index(drop=True)
            bundes_shot.append(bundes_shot)
        except:
            continue
        
bundes_shot["90s"] = pd.to_numeric(bundes_shot["90s"])
bundes_shot["Age"] = pd.to_numeric(bundes_shot["Age"])
bundes_shot["xG"] = pd.to_numeric(bundes_shot["xG"])
bundes_shot["npxG"] = pd.to_numeric(bundes_shot["npxG"])
bundes_shot["xG/90"] = bundes_shot["xG"]/bundes_shot["90s"]
bundes_shot["npxG/90"] = bundes_shot["npxG"]/bundes_shot["90s"]
bundes_shot = bundes_shot[bundes_shot["Age"] <=30]
bundes_shot = bundes_shot[bundes_shot["90s"] >=15]
bundes_shot=bundes_shot[(bundes_shot["Pos"]=="FW,MF") | (bundes_shot["Pos"]=="FW") | (bundes_shot["Pos"]=="MF,FW")]



bundes_gca_url = 'https://fbref.com/en/comps/20/gca/Bundesliga-Stats#stats_gca'
response = requests.get(bundes_gca_url)

tables = pd.read_html(response.text, header=1)

# Get the tables within the Comments
soup = BeautifulSoup(response.text, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for each in comments:
    if 'table' in str(each):
        try:
            bundes_gca = pd.read_html(str(each), header=1)[0]
            bundes_gca = bundes_gca[bundes_gca['Rk'].ne('Rk')].reset_index(drop=True)
            bundes_gca.append(bundes_gca)
        except:
            continue
        
bundes_gca["90s"] = pd.to_numeric(bundes_gca["90s"])
bundes_gca["Age"] = pd.to_numeric(bundes_gca["Age"])
bundes_gca["SCA"] = pd.to_numeric(bundes_gca["SCA"])
bundes_gca["GCA"] = pd.to_numeric(bundes_gca["GCA"])
bundes_gca["SCA90"] = pd.to_numeric(bundes_gca["SCA90"])
bundes_gca["GCA90"] = pd.to_numeric(bundes_gca["GCA90"])
#epl_shot["xG/90"] = epl_shot["xG"]/epl_shot["90s"]
#epl_shot["npxG/90"] = epl_shot["npxG"]/epl_shot["90s"]
#epl_shot["Age"]=epl_shot["Age"]<=30
bundes_gca = bundes_gca[bundes_gca["Age"] <=30]
bundes_gca = bundes_gca[bundes_gca["90s"] >=15]
#epl_shot=epl_shot["90s"]>=15
bundes_gca=bundes_gca[(bundes_gca["Pos"]=="FW,MF") | (bundes_gca["Pos"]=="FW") | (bundes_gca["Pos"]=="MF,FW")]
bundesliga= pd.merge( bundes_gca, bundes_shot, on=["Rk","Player","Nation","Pos","Squad","Age","Born","90s","Matches"])

##########################################################################################################################

ligue1_shot_url = 'https://fbref.com/en/comps/13/shooting/Ligue-1-Stats#stats_shooting'
response = requests.get(ligue1_shot_url)

tables = pd.read_html(response.text, header=1)

# Get the tables within the Comments
soup = BeautifulSoup(response.text, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for each in comments:
    if 'table' in str(each):
        try:
            ligue1_shot = pd.read_html(str(each), header=1)[0]
            ligue1_shot = ligue1_shot[ligue1_shot['Rk'].ne('Rk')].reset_index(drop=True)
            ligue1_shot.append(ligue1_shot)
        except:
            continue
        
ligue1_shot["90s"] = pd.to_numeric(ligue1_shot["90s"])
ligue1_shot["Age"] = pd.to_numeric(ligue1_shot["Age"])
ligue1_shot["xG"] = pd.to_numeric(ligue1_shot["xG"])
ligue1_shot["npxG"] = pd.to_numeric(ligue1_shot["npxG"])
ligue1_shot["xG/90"] = ligue1_shot["xG"]/ligue1_shot["90s"]
ligue1_shot["npxG/90"] = ligue1_shot["npxG"]/ligue1_shot["90s"]
ligue1_shot = ligue1_shot[ligue1_shot["Age"] <=30]
ligue1_shot = ligue1_shot[ligue1_shot["90s"] >=15]
ligue1_shot=ligue1_shot[(ligue1_shot["Pos"]=="FW,MF") | (ligue1_shot["Pos"]=="FW") | (ligue1_shot["Pos"]=="MF,FW")]



ligue1_gca_url = 'https://fbref.com/en/comps/13/gca/Ligue-1-Stats#stats_gca'
response = requests.get(ligue1_gca_url)

tables = pd.read_html(response.text, header=1)

# Get the tables within the Comments
soup = BeautifulSoup(response.text, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
for each in comments:
    if 'table' in str(each):
        try:
            ligue1_gca = pd.read_html(str(each), header=1)[0]
            ligue1_gca = ligue1_gca[ligue1_gca['Rk'].ne('Rk')].reset_index(drop=True)
            ligue1_gca.append(ligue1_gca)
        except:
            continue
        
ligue1_gca["90s"] = pd.to_numeric(ligue1_gca["90s"])
ligue1_gca["Age"] = pd.to_numeric(ligue1_gca["Age"])
ligue1_gca["SCA"] = pd.to_numeric(ligue1_gca["SCA"])
ligue1_gca["GCA"] = pd.to_numeric(ligue1_gca["GCA"])
ligue1_gca["SCA90"] = pd.to_numeric(ligue1_gca["SCA90"])
ligue1_gca["GCA90"] = pd.to_numeric(ligue1_gca["GCA90"])
#epl_shot["xG/90"] = epl_shot["xG"]/epl_shot["90s"]
#epl_shot["npxG/90"] = epl_shot["npxG"]/epl_shot["90s"]
#epl_shot["Age"]=epl_shot["Age"]<=30
ligue1_gca = ligue1_gca[ligue1_gca["Age"] <=30]
ligue1_gca = ligue1_gca[ligue1_gca["90s"] >=15]
#epl_shot=epl_shot["90s"]>=15
ligue1_gca=ligue1_gca[(ligue1_gca["Pos"]=="FW,MF") | (ligue1_gca["Pos"]=="FW") | (ligue1_gca["Pos"]=="MF,FW")]
ligue1= pd.merge( ligue1_gca, ligue1_shot, on=["Rk","Player","Nation","Pos","Squad","Age","Born","90s","Matches"])

####################################################################################################################

fwd_table = pd.merge( laliga, prem, how="outer") #Merge all tables
fwd_table = pd.merge(fwd_table,seriea, how="outer")
fwd_table = pd.merge(fwd_table,bundesliga, how="outer")
fwd_table = pd.merge(fwd_table,ligue1, how="outer")

fwd_table = fwd_table.sort_values(["GCA90","xG/90"], ignore_index=True)
fwd_table.loc[1:54,['Player']] = ['']
#fwd_table.loc[55:195,['Player']] = ['']
fwd_table.loc[55:72,['Player']] = ['']
fwd_table.loc[74:96,['Player']] = ['']
fwd_table.loc[98:102,['Player']] = ['']
fwd_table.loc[104:193,['Player']] = ['']
#fwd_table.loc[197:240,['Player']] = ['']
fwd_table.loc[195:206,['Player']] = ['']
fwd_table.loc[208:218,['Player']] = ['']
fwd_table.loc[220:230,['Player']] = ['']
fwd_table.loc[232:237,['Player']] = ['']
fwd_table.loc[239:240,['Player']] = ['']
fwd_table.loc[242:256,['Player']] = ['']
fwd_table.loc[258:271,['Player']] = ['']
fwd_table.loc[273,['Player']] = ['']
fwd_table.loc[274:279,['Player']] = ['']
fwd_table.loc[281:285,['Player']] = ['']
fwd_table.loc[287:292,['Player']] = ['']
fwd_table.loc[298,['Player']] = ['']
#fwd_table = fwd_table.reset_index(drop=True)


#######################################################################################################################

a = fwd_table['xG/90']
b = fwd_table['GCA90']
d= fwd_table['Player']
plt.rcParams.update({'font.family':'Avenir'})
bgcol = '#2B547E'

#mpl.rcParams['text.color'] = 'white'

fig, ax = plt.subplots(figsize=(6, 4), dpi=120)
ax.scatter(a,b, color = "white")
fig.set_facecolor(bgcol)
ax.set_facecolor(bgcol)
ax.scatter(a, b, color='#ffa500')

fig= plt.figure(1, figsize=(8, 14), frameon=False, dpi=100)
for x,y,z in zip(a,b,d):
    label = "{}".format(z)
    plt.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center')
plt.ylabel('GCA/90',color='white')
plt.xlabel('xG/90',color='white')
plt.hlines(fwd_table['GCA90'].mean(), fwd_table['xG/90'].min(), fwd_table['xG/90'].max(), color='#c2c1c0')
plt.vlines(fwd_table['xG/90'].mean(), fwd_table['GCA90'].min(), fwd_table['GCA90'].max(), color='#c2c1c0')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#ccc8c8')
ax.spines['bottom'].set_color('#ccc8c8')

plt.text(0,1.2,'Comparing Forwards in the T5 leagues \n based on Goal creating actions and xG', size=9.5, color='white')

fig.savefig('/Users/damianesene/Downloads/sadio_xg_gca.jpg', dpi=300)


