
import pandas as pd # biblioteca DataFrames
import numpy as np # biblioteca de  calculos matemáticos
import matplotlib.pyplot as plt #  biblioteca de criação de gráficos
import seaborn as sns # biblioteca de gráficos mais atraentes

covid = pd.read_csv("caso_full.csv",encoding='ISO-8859-1')
#print(covid.head(10)) #impressão das 10 primeiras linhas

covid = covid.dropna(subset=['city'], axis=0) #Apago registros de cidade em branco

#Analisar por estado novos casos
casos_covid = {}
nomes_estado = covid['state'].unique() #Nome de estado  que aparece no arquivo


for i in nomes_estado:
    i_estado = covid[covid['state'] == i]  # Série criada somente onde o nome do atual estado aparece
    total_de_casos = i_estado['new_confirmed'].sum()  # Soma de todas os novos casos do estado
    casos_covid[i] = total_de_casos  # Criando chave e valor no dicionário
    total_estado = pd.DataFrame.from_dict(casos_covid, orient='index')  # Criando DataFrame com base no dicionário
    total_estado.columns = ['TOTAL_CASOS']  # Renomeando a coluna com valor


total_estado = total_estado.sort_values('TOTAL_CASOS', ascending=False)  # Ordeno valores do DF
total_estado.head(25).plot(kind='barh', figsize=(10, 5), color='green', legend=False, grid=True, alpha=0.7)  # 
plt.show()




