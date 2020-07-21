import pandas as pd
import plotly.graph_objects as go
import plotly.offline as py
import plotly.graph_objs as go

covid = pd.read_csv("caso_full.csv",encoding='ISO-8859-1')

#Analisar por estado novos casos
casos_covid = {}
nomes_estado = covid['state'].unique() #Nome de estado  que aparece no arquivo

for i in nomes_estado:
    i_estado = covid[covid['state'] == i]  # Série criada somente onde o nome do atual estado aparece
    total_de_casos = i_estado['new_confirmed'].sum()  # Soma de todas os novos casos do estado
    print(total_de_casos)
    casos_covid[i] = total_de_casos/2
    total_estado = pd.DataFrame.from_dict(casos_covid, orient='index')  # Criando DataFrame com base no dicionário
    total_estado.columns = [ 'TOTAL_CASOS']  # Renomeando a coluna com valor



total_estado = total_estado.sort_values('TOTAL_CASOS', ascending=False)  # Ordeno valores do DF
print(total_estado)


trace = go.Scatter(x = nomes_estado,
                  y = total_estado['TOTAL_CASOS'],
                  mode = 'markers+lines',
                  name = 'Total de Casos por UF')





data = [trace ]
layout = go.Layout(title='Total de Casos por UF',
                yaxis={'title':'Casos'},
                xaxis={'title': 'UF'})
fig = go.Figure(data=data, layout=layout)
fig.show()
