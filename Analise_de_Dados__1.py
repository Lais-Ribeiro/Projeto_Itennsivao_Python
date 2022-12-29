import pandas as pd
from IPython.display import display
import plotly.express as px

pd.set_option('display.max_columns', None)

#Importando a base de dados
tabela_clientes = pd.read_csv(r'C:\Users\lais_\Desktop\GitHub\Projeto_Itennsivao_Python\ClientesBanco.csv', encoding='latin1')

#Excluindo colunas desnecessárias
tabela_clientes = tabela_clientes.drop("CLIENTNUM", axis=1)

#Excluindo a linha que possui valor nulo
tabela_clientes = tabela_clientes.dropna()

#Verficando a quantidade de clientes, quantos estão ativos e quantos estão cancelados com os número
display(tabela_clientes['Categoria'].value_counts())

#Verficando a quantidade de clientes, quantos estão ativos e quantos estão cancelados com os percentuais
display(tabela_clientes['Categoria'].value_counts(normalize=True))

for coluna in tabela_clientes:
    #criando a figura do gráfico
    fig = px.histogram(tabela_clientes, x=coluna, color="Categoria")
    #Exibindo o gráfico
    fig.show()