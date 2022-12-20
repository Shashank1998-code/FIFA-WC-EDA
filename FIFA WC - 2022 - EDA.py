#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import pandas as pd
import numpy as np
import plotly.express as px


# In[5]:


fifa = pd.read_csv("C:/Users/shash/Desktop/FIFA_WC_22.csv", encoding = 'latin1')


# In[6]:


fifa.tail()


# In[7]:


fifa.info()
# Checking For Null Values 
fifa.isnull().sum()


# In[8]:


fifa['total_match_goals'] = fifa['1_goals'] + fifa['2_goals']


# In[10]:


#Most Goals Scored in a match 

fifa[fifa['total_match_goals'] == fifa['total_match_goals'].max()]


# In[11]:


#Highest Attendance for a single match 

fifa[fifa['attendance'] == fifa['attendance'].max()]


# In[12]:


#No of Games played across each Venue 

fifa['venue'].value_counts()


# In[15]:


# Bar graph of Stadium v/s No of Matches Played at Venue (using plotly)
x = fifa['venue'].value_counts().index
y = fifa['venue'].value_counts().values

df = pd.DataFrame({'Venue':x,
                  'Matches':fifa['venue'].value_counts().values })

fig = px.bar(df, 
             x='Venue', 
             y='Matches',
             color='Venue',
             title='Stadium v/s No of Matches Played at each Stadium'
            )
fig.show()


# In[16]:


#Grouping attendance across Venues

fifa.groupby('venue').sum()['attendance'].sort_values(ascending=False)


# In[36]:




# Bar graph venue v/s attendance at Venue 
x = fifa.groupby('venue').sum()['attendance'].sort_index().index
y = fifa.groupby('venue').sum()['attendance'].sort_index().values

df_1 = pd.DataFrame({'venue': x, 'attendance': y})

fig = px.bar(df_1, x='venue', y='attendance',color='attendance',title='Stadium v/s Total Attendance of all matches played')
fig.update_layout(title_text='Stadium v/s Total Attendance of all matches played',template='plotly_dark')
fig.show()


# In[40]:


team_df = pd.DataFrame({'teams':fifa['1'].value_counts().sort_index().index,
                        'total_matches':fifa['1'].value_counts().sort_index().values + fifa['2'].value_counts().sort_index().values,
                        'total_goals': fifa.groupby(['1'])['1_goals'].sum().sort_index().values + fifa.groupby(['2'])['2_goals'].sum().sort_index().values, 
                         })
team_df.sort_values(by='total_goals', ascending=False)


# In[45]:


fig = px.bar(team_df, x='teams', y='total_goals',title='Teams v/s Goals Scored')
fig.show()


# In[48]:


# Top 3 highest Goal Scoring Teams
team_df.sort_values(by='total_goals', ascending=False).head(3)


# In[54]:


team_df['total_pass_completed'] = fifa.groupby(['1'])['1_passes_compeletd'].sum().sort_index().values 
+ fifa.groupby(['2'])['2_passes_compeletd'].sum().sort_index().values

fig = px.bar(team_df, x='teams', y='total_pass_completed',title='Teams v/s Pass Completed')
fig.show()


# In[63]:


# Bar graph Teams v/s Avg Possession 

team_df['avg_possession'] = round((fifa.groupby(['1'])['1_poss'].sum().sort_index().values
                                   + fifa.groupby(['2'])['2_poss'].sum().sort_index().values)/team_df['total_matches'], 2)

fig = px.bar(team_df, x='teams', y='avg_possession', title='Teams v/s Avg Possession')
fig.update_layout(title_text='Teams v/s Avg Possession ',template='ggplot2')
fig.show()


# In[60]:




# Bar graph Teams v/s Total Goals Conceded

team_df['total_goals_conceded'] = (fifa.groupby(['1'])['1_conceded'].sum().sort_index().values 
                                   + fifa.groupby(['2'])['2_conceded'].sum().sort_index().values)


fig = px.bar(team_df, x='teams', y='total_goals_conceded',title='Teams v/s Total Goals Conceded ')
fig.update_layout(title_text='Teams v/s Total Goals Conceded  ',template='none')
fig.show()


# In[67]:


player_stat = pd.read_csv("C:/Users/shash/Desktop/FIFA EDA/player_stats.csv", encoding='latin1')


# In[68]:


player_stat.tail()


# In[69]:




# Top 5 Goal Scorer of WC 2022
player_stat.loc[:, ['player', 'team','birth_year', 'club','games', 'assists','goals' ] ].sort_values(by='goals', ascending=False).head(5)


# In[70]:




# Top Assist Providers of WC 2022 
player_stat.loc[player_stat_df['assists'] == player_stat_df['assists'].max(),
                ['player', 'team','birth_year', 'club','games', 'assists','goals' ] ].sort_values(by='goals', ascending=False).head(5)


# In[88]:




player_stat.loc[:, ['player', 'team','birth_year', 'club','games', 'assists','goals','xg','xg_per90','npxg_per90','xg_assist_per90' ] ].sort_values(by='xg', ascending=False).head(5)

