import pandas as pd
import os

#configs
raw_data = 'data/raw_data'

#país
countryColum = 'delivery_country'

#preços totais
totalPriceColum = 'total_price'

#processamento e listagem dos dados
allDateProcessed = [] 

print(f"Procurando arquivos: {raw_data}")

#verificando se a pasta realmente existe
if not os.path.isdir(raw_data):
    print(f"Erro: A pasta '{raw_data}' não foi encontrada.")
else:
    #listando todos os arquivos
    for arquivoCSV in os.listdir(raw_data):
        #verificando se o item na pasta é um arquivo csv
        lendoColunas = os.path.join(raw_data, arquivoCSV)
        if os.path.isfile(lendoColunas) and arquivoCSV.endswith('.csv'):
            print(f"Lendo arquivo: {arquivoCSV}") #mostrando apenas o nome do arquivo
            try:
                #lendo o arquivo CSV
                df = pd.read_csv(lendoColunas)
                allDateProcessed.append(df)
            except Exception as e:
                print(f"Erro ao ler o arquivo {arquivoCSV}: {e}") #continua para o proximo arquivo

#resumindo os dados
if not allDateProcessed:
    print("Nenhum arquivo CSV encontrado.")
else:
    #concatenando todos os dados
    gerDados = pd.concat(allDateProcessed, ignore_index=True)
    print("\nDados processados")

    #verificando se as colunas existem
    if countryColum not in gerDados.columns:
        print(f"Erro: A coluna '{countryColum}' não foi encontrada.")
    elif totalPriceColum not in gerDados.columns:
         print(f"Erro: A coluna '{totalPriceColum}' não foi encontrada.")
    else:
        #agrupando por país e somar as vendas
        #.reset_index() transforma o país
        sellPerCountry = gerDados.groupby(countryColum)[totalPriceColum].sum().reset_index()

        #ordenanado por total de vendas
        sellPerCountry = sellPerCountry.sort_values(by=totalPriceColum, ascending=False)

        #resultado
        print("\nVendas por País")
        print(sellPerCountry)
