import pandas as pd
import plotly.graph_objects as go


import plotly.offline as py
import plotly.graph_objs as go


df_saopaulo = pd.read_csv('saopaulo.csv' , sep=',')
df_barretos = pd.read_csv('barretos.csv' , sep=',')
df_vitoria = pd.read_csv('vitoria.csv' , sep=',')



df_barretos = go.Scatter(x = df_barretos['date'],
                   y = df_barretos['new_confirmed'],
                   mode = 'lines',
                   name = 'Barretos')

df_vitoria = go.Scatter(x = df_vitoria['date'],
                   y = df_vitoria['new_confirmed'],
                   mode = 'lines',
                   name = 'Vitória')


data = [ df_barretos, df_vitoria ]
layout = go.Layout(title='Evolução COVID-19 Barretos x Vitória',
                   yaxis={'title':'Novos Casos'},
                   xaxis={'title': 'Data'})
fig = go.Figure(data=data, layout=layout)
fig.show()
