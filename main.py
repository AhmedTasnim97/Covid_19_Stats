#!/usr/bin/env python
# coding: utf-8




import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
import requests
get_ipython().run_line_magic('matplotlib', 'inline')





url = 'https://api.covid19india.org/data.json'
jsn = requests.get(url).json()





cumul=jsn['cases_time_series']
daily=[int(i['totalconfirmed']) for i in cumul]
dates = [i['date'] for i in cumul]


dic={'Daily_Total':daily,'Day':dates}
df = pd.DataFrame(dic)


fig = px.line(df, x='Day', y='Daily_Total')
fig.show()





state_wise_data=jsn['statewise']

col=list(state_wise_data[0].keys())





state_data = []
for i in col:
    state_data.append([j[i] for j in state_wise_data])





dic={col[i]:state_data[i] for i in range(12)}





df1=pd.DataFrame(dic)
df1["Country"]='India'
df1['active'] = list(map(int , df1['active']))
df1['confirmed'] = list(map(int, df1['confirmed']))
df1['recovered'] = list(map(int, df1['recovered']))
df1['deaths'] = list(map(int, df1['deaths']))
df1['deltaconfirmed'] = list(map(int, df1['deltaconfirmed']))
df1['deltarecovered'] = list(map(int, df1['deltarecovered']))
df1['migratedother'] = list(map(int, df1['migratedother']))











df1=df1.drop([0])






df1['tokens']=np.array(range(38,1,-1))





time=list(df1['lastupdatedtime'])





dfx = pd.DataFrame(dic)
dfx["Country"]='India'
dfx['active'] = list(map(int , dfx['active']))





fig = px.scatter(dfx.query("Country=='India'"), 
                 x="active", y="recovered",
           size="active", color="state", 
                 hover_name='active', log_x=True, size_max=60)
fig.update_layout(title='Covid 19 statistics'+' last updated time '+str(pd.to_datetime(dfx['lastupdatedtime']).max()))
fig.show()

