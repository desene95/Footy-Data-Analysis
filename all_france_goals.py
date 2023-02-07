#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 20:06:12 2023

@author: damianesene
"""

import matplotlib.pyplot as plt

from mplsoccer import VerticalPitch, FontManager, Sbopen

parser = Sbopen()

df_comp = parser.competition()

df_match = parser.match(competition_id=43, season_id=106)
df_france_home = df_match[(df_match["home_team_name"]=="France") | (df_match["away_team_name"]=="France")]
#all_goal_ids = 
#df_france_away = df_match[((df_match["away_team_name"]=="France"))]
print("France Game IDs:\n",df_france_home["match_id"].to_string(index=False))
game_id = input("What game do you want plotted? ")
df_event_1, df_related_1, df_freeze_1, df_tactics_ = parser.event(game_id)
all_goals = df_event_1[(df_event_1["outcome_name"]=="Goal")]

print("Here are the Goal IDs for this game:\n",all_goals["id"].to_string(index=False))
match_goal_id = input("What Goal ID? ")
saved_img_name = input("What do you want to save this image/plot as? ")

def goals_in_FRA_games(game_id,match_goal_id,saved_img_name):
     #first game
    df_lineup_1 = parser.lineup(game_id)
    #mbappe_tbl_1 = df_event_1[(df_event_1['player_name'] == 'Kylian Mbappé Lottin')]
    #goal_tbl_1 = mbappe_tbl_1[(mbappe_tbl_1['outcome_name']=='Goal')]
    goal_id_1 = match_goal_id
    
    df_freeze_frame_1 = df_freeze_1[df_freeze_1.id == goal_id_1].copy()
    df_goal_event_1 = df_event_1[df_event_1.id == goal_id_1].dropna(axis=1, how='all').copy()
    df_freeze_frame_1 = df_freeze_frame_1.merge(df_lineup_1, how='left', on='player_id')
    
    team1 = df_goal_event_1.team_name.iloc[0]
    team2 = list(set(df_event_1.team_name.unique()) - {team1})[0]
    
    df_team1 = df_freeze_frame_1[df_freeze_frame_1.team_name == team1]
    
    df_team2_goal = df_freeze_frame_1[(df_freeze_frame_1.team_name == team2) &
                                     (df_freeze_frame_1.position_name == 'Goalkeeper')] 
    #Get position of other defending team players
    df_team2_other = df_freeze_frame_1[(df_freeze_frame_1.team_name == team2) &
                                     (df_freeze_frame_1.position_name != 'Goalkeeper')]
    
    pitch = VerticalPitch(half=True, goal_type='box', pad_bottom=-20)
    fig, axs = pitch.grid(figheight=8, endnote_height=0,  # no endnote
                           title_height=0.1, title_space=0.02,
                           # turn off the endnote/title axis. i usually do this after
                           # i am happy with the chart layout and text placement
                           axis=False,
                           grid_height=0.83)
    
    #Plot the players
    sc_team1 = pitch.scatter(df_team1.x, df_team1.y, s=600, c='#727cce', label='Attacker', ax=axs['pitch']) #attacking players
    sc_team2 = pitch.scatter(df_team2_other.x, df_team2_other.y, s=600,
                        c='#5ba965', label='Defender', ax=axs['pitch']) #defending players
    sc_team2_goalie = pitch.scatter(df_team2_goal.x, df_team2_goal.y, s=600,
                        ax=axs['pitch'], c='#c15ca5', label='Goalkeeper') #defending goalie
    
    sc_shot = pitch.scatter(df_goal_event_1.x, df_goal_event_1.y, marker='football',
                        s=600, ax=axs['pitch'], label='Shooter', zorder=1.2) #the shot itself
    line = pitch.lines(df_goal_event_1.x, df_goal_event_1.y,
                       df_goal_event_1.end_x, df_goal_event_1.end_y, comet=True,
                       label='shot', color='#cb5a4c', ax=axs['pitch'])
    # plot the angle to the goal
    pitch.goal_angle(df_goal_event_1.x, df_goal_event_1.y, ax=axs['pitch'], alpha=0.2, zorder=1.1,
                     color='#cb5a4c', goal='right')
    
    # fontmanager for google font (robotto)
    robotto_regular = FontManager()
    
    # plot the jersey numbers
    for i, label in enumerate(df_freeze_frame_1.jersey_number):
        pitch.annotate(label, (df_freeze_frame_1.x[i], df_freeze_frame_1.y[i]),
                       va='center', ha='center', color='white',
                       fontproperties=robotto_regular.prop, fontsize=15, ax=axs['pitch'])
    
    # add a legend and title
    legend = axs['pitch'].legend(loc='center left', labelspacing=1.5)
    for text in legend.get_texts():
        text.set_fontproperties(robotto_regular.prop)
        text.set_fontsize(20)
        text.set_va('center')
    
    # title
    axs['title'].text(0.5, 0.5, f'{df_goal_event_1.player_name.iloc[0]}\n{team1} vs. {team2}\n{all_goals.timestamp.iloc[1]}',
                      va='center', ha='center', color='black',
                      fontproperties=robotto_regular.prop, fontsize=25)
    
    plt.show()  # If you are using a Jupyter notebook you do not need this line
    fig.savefig(f'/Users/damianesene/Downloads/{saved_img_name}.jpg', dpi=300)

goals_in_FRA_games(game_id,match_goal_id,saved_img_name)


