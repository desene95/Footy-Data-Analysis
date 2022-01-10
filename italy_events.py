#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 18:03:45 2021

@author: damianesene
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc #creates the patches
import json #reads json file
import matplotlib.patches as mpatches



match_id_required = 3795220 #Match Id from Json file

#Pitch Dimension
pitchLengthX=120
pitchWidthY=80

home_team_required = "Spain"
away_team_required = "Italy"

#load the data
file_name = str(match_id_required)+'.json'

#load in all match events
with open('/Users/damianesene/Downloads/open-data-master-3/data/events/'+file_name) as data_file:
    data = json.load(data_file)
    
#defines a dataframe
 #=============================================================================
from pandas.io.json import json_normalize
df = json_normalize(data, sep = "_").assign(match_id = file_name[:-5])
# =============================================================================


#press_data = pd.read_excel('/Users/damianesene/Documents/open-data/data/events/FRA_COR_corners')
#creates shots data frame

#Create a DF for just Italy
Italy =df[df['team_name']=='Italy']
Italy=Italy.dropna(subset=['location']) #drop valuses with n/a in location column

#create a df for just italy goals
Italy_Goals = Italy[Italy['shot_outcome_name']=='Goal']

#Create a DF for just Italy passes
Italy_Pass = Italy[Italy['type_name']=='Pass']
from fcpython import createPitch #Creates pitch
(fig,ax) = createPitch(pitchLengthX,pitchWidthY,'yards','gray')
# =============================================================================
# for i,shots in Italy_Goals.iterrows():
#     x=shots['location'][0]
#     y=shots['location'][1]
#     dx=shots['shot_end_location'][0]-x
#     dy=shots['shot_end_location'][1]-y
#     circleSize=2
#     team_name=shots['team_name']
#     #team_corner=passes['pass_type_name'] == 'Corner'
#     #team_name=passes['team_name']
#     if (team_name==away_team_required and shots['shot_type_name']!= 'Penalty' ):
#         
#         plt.xlim(0,120)
#         plt.ylim(0,80)
#         shotCircle=plt.Circle((pitchLengthX-x,y),circleSize,color="blue")
#         carryarrow=plt.Arrow(pitchLengthX-x,y,-(pitchLengthX-x),dy,width=3,color="red")
#         #plt.text((x+1),pitchWidthY-y+1,shots['player_name'])
#         plt.text((pitchLengthX-x+1),y+1,shots['player_name']) 
#         ax.add_patch(carryarrow)
#         ax.add_patch(shotCircle)
# =============================================================================
#Create a DF that has sequence os play from index 2187 to 2199. Those indexes show the sequence of play that happened in the 52nd minute
italy_sq1 = Italy.loc[2187:2199]

#Itearte through each action
for j,passes in italy_sq1.iterrows():
    a=passes['location'][0]
    b=passes['location'][1]   
    #da=passes['shot_end_location'][0]-a
    #db=passes['shot_end_location'][1]-b 
    #da=passes.loc['type_name']['location'][0]-a
   # db=passes.loc['type_name']['location'][1]-b
    circleSize=2
    team_name=passes['team_name']
    #team_corner=passes['pass_type_name'] == 'Corner'
    #team_name=passes['team_name']
    if (team_name==away_team_required):
        
        plt.xlim(0,120)
        plt.ylim(0,80)
        passCircle=plt.Circle((pitchLengthX-a,b),circleSize,color="blue")
        #passarrow=plt.Arrow(pitchLengthX-a,b,-(pitchLengthX-a),db,width=3,color="red")
        plt.text((pitchLengthX-a+1),b+1,passes['player_name']) 
        #plt.text((pitchLengthX-x+1),y+1,passes['player_name']) 
        #ax.add_patch(passarrow)
        ax.add_patch(passCircle)
for k,shot in italy_sq1.iterrows():
    if (shot['type_name']=='Shot'):
        
        c=shot['location'][0]
        d=shot['location'][1] 
        dc=shot['shot_end_location'][0]-c
        dd=shot['shot_end_location'][1]-d
   
        circleSize=2
        #team_name=passes['team_name']
        plt.xlim(0,120)
        plt.ylim(0,80)
        shotCircle=plt.Circle((pitchLengthX-a,b),circleSize,color="blue")
        shotarrow=plt.Arrow(pitchLengthX-c,d,-(pitchLengthX-c),dd,width=3,color="red")
        plt.text((pitchLengthX-a+1),b+1,passes['player_name']) 
        #plt.text((pitchLengthX-x+1),y+1,passes['player_name']) 
        ax.add_patch(shotarrow)
        ax.add_patch(shotCircle)
        #team_corner=passes['pass_type_name'] == 'Corner'
        #team_name=passes['team_name']
   
for l,passing in italy_sq1.iterrows():
    if (passing['type_name']=='Pass'):
        
        e=passing['location'][0]
        f=passing['location'][1] 
        de=passing['pass_end_location'][0]-e
        df=passing['pass_end_location'][1]-f
        
        circleSize=2
        #team_name=passes['team_name']
        plt.xlim(0,120)
        plt.ylim(0,80)
        passingCircle=plt.Circle((pitchLengthX-e,f,),circleSize,color="blue")
        passingarrow=plt.Arrow(pitchLengthX-e,f,-(de),df,width=3,color="green")
        plt.text((pitchLengthX-a+1),b+1,passes['player_name']) 
        #plt.text((pitchLengthX-x+1),y+1,passes['player_name']) 
        ax.add_patch(passingarrow)
        ax.add_patch(passingCircle)
        #team_corner=passes['pass_type_name'] == 'Corner'
        #team_name=passes['team_name']
for m,carry in italy_sq1.iterrows():
    if (carry['type_name']=='Carry'):
        
        g=carry['location'][0]
        h=carry['location'][1] 
        dg=carry['carry_end_location'][0]-g
        dh=carry['carry_end_location'][1]-h
        
        circleSize=2
        #team_name=passes['team_name']
        plt.xlim(0,120)
        plt.ylim(0,80)
        carryCircle=plt.Circle((pitchLengthX-g,h,),circleSize,color="blue")
        carryarrow=plt.Arrow(pitchLengthX-g,h,-(dg),dh,width=3,color="black")
        plt.text((pitchLengthX-a+1),b+1,passes['player_name']) 
        #plt.text((pitchLengthX-x+1),y+1,passes['player_name']) 
        ax.add_patch(carryarrow)
        ax.add_patch(carryCircle)
        #team_corner=passes['pass_type_name'] == 'Corner'
        #team_name=passes['team_name']
        
#Plot title and other texts
plt.title('Italy shot on target  in the 52nd Minute ')
plt.text(5,75,away_team_required + ' attacking') 
#================================================================ Description of arrows
left, bottom, width, height = (5, 5, 5, 2)
rect=mpatches.Rectangle((left,bottom),width,height, 
                        fill=True,
                        color="green",
                       linewidth=2)
                       #facecolor="red")
plt.gca().add_patch(rect)
plt.text(11,5, "- Pass")
#================================================================
left, bottom, width, height = (5, 3, 5, 2)
rect=mpatches.Rectangle((left,bottom),width,height, 
                        fill=True,
                        color="black",
                       linewidth=2)
                       #facecolor="red")
plt.gca().add_patch(rect)
plt.text(11,3, "- Carry")
#================================================================
left, bottom, width, height = (5, 1, 5, 2)
rect=mpatches.Rectangle((left,bottom),width,height, 
                        fill=True,
                        color="red",
                       linewidth=2)
                       #facecolor="red")
plt.gca().add_patch(rect)
plt.text(11,1, "- Shot")
#================================================================
plt.text(80,75,home_team_required + ' attacking') 
fig.set_size_inches(15, 8)
fig.savefig('/Users/damianesene/Downloads/italy_events.jpg', dpi=300)
