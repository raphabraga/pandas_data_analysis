import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

df = pd.read_excel("./dataset/AdventureWorks.xlsx")

#Calculando a receita total
rec_tot = df['Valor Venda'].sum()
print(rec_tot)

#Adicionando um nova coluna para o dataframe com o custo por produto
df['Custo'] = df['Custo Unitário'].mul(df['Quantidade'])
print(df.head(1))

#Calculando o custo total
cust_tot = round(df['Custo'].sum(),2)
print(cust_tot)

#Adicionando uma nova coluna para o dataframe com o lucro por produto
df["Lucro"] = df['Valor Venda'] - df['Custo']
print(df.head(1))

#Calculando o lucro total
luc_tot = round(df['Lucro'].sum(),2)
print(luc_tot)

#Adicionando uma nova coluna para o dataframe como o tempo em dias para envio do produto
df["Tempo de Envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days
print(df.head(1))

#Calculando a media de tempo de envio por Marca
tempo_envia_por_marca = df.groupby("Marca")['Tempo de Envio'].mean()
print(tempo_envia_por_marca)

#Checando a presenca de dados faltantes
print(df.isnull().sum())

#Calculando o lucro por ano e por marca
print(df.groupby([df["Data Venda"].dt.year,"Marca"])["Lucro"].sum())

#Ajustando o formato de numeros ponto flutuantes
pd.options.display.float_format = "{:20,.2f}".format

#Resetando o index
lucro_ano_marca = df.groupby([df["Data Venda"].dt.year,"Marca"])["Lucro"].sum().reset_index()
print(lucro_ano_marca)

#Total de produtos vendidos 
print(df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False))

#Plotando em grafico de barra horizontais das informacoes de total de produtos vendidos
total_prod_barh = df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=True).plot.barh(title="Total de produtos vendidos")
plt.xlabel("Ano")
plt.ylabel("Produto")
plt.savefig('Total de Produtos Vendidos.png')
plt.clf()

#Plotando o grafico de barras verticais do lucro por ano
lucro_ano_bar = df.groupby(df["Data Venda"].dt.year)["Lucro"].sum().plot.bar(title = 'Lucro x Ano')
plt.xlabel('Ano')
plt.ylabel('Receita')
plt.savefig('Lucro por Ano.png')
plt.clf()

#Filtrando as vendas que ocorreram no ano de 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]

#Plotando o grafico de lucro por mes em 2009
lucro_2009_month = df_2009.groupby(df_2009['Data Venda'].dt.month)['Lucro'].sum().plot(title = 'Lucro x Mes')
plt.xlabel("Mes")
plt.ylabel('Lucro')
plt.savefig('Lucro por mes em 2009.png')
plt.clf()

#Plotando o grafico de lucro por marca em 2009
lucro_2009_brand = df_2009.groupby('Marca')['Lucro'].sum().plot.bar(title = 'Lucro x Marca')
plt.xlabel("Marca")
plt.ylabel('Lucro')
plt.xticks(rotation='horizontal')
plt.savefig('Lucro por marcar em 2009.png')
plt.clf()

#Plotando o grafico de lucro por classe em 2009
lucro_2009_classe = df_2009.groupby('Classe')['Lucro'].sum().plot.bar(title = 'Lucro x Classe')
plt.xlabel("Classe")
plt.ylabel('Lucro')
plt.xticks(rotation='horizontal')
plt.savefig('Lucro por classe em 2009.png')
plt.clf()

#Plotando o grafico Boxplot para analise estatistica dos dados
df_boxplot = plt.boxplot(df['Tempo de Envio'])
plt.savefig('Boxplot do tempo de envio.png')
plt.clf()

#Plotando o histograma dos dados
df_hist = plt.hist(df['Tempo de Envio'])
plt.savefig('Histograma do tempo de envio.png')
plt.clf()

#Calculando o tempo de envio maximo
max_tempo_envio = df['Tempo de Envio'].max()
print(max_tempo_envio)

#Imprimindo a linha com tempo de envio discrepante
print(df[df['Tempo de Envio'] == max_tempo_envio])

#Salvando o dataframe manipulando na pasta do projeto
df.to_csv('df_vendas_novo.csv', index=False)