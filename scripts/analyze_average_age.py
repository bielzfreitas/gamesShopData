import pandas as pd
import os
from datetime import date #import do módulo datetime para trabalhar com datas
 
# --- Configurações ---
#pasta onde os arquivos CSVs estão localizados
raw_data = 'data/raw_data'

#coluna que contém os países
countryColum = 'delivery_country' 

#coluna que contém os produtos
productSoldColum = 'product_sold'

#coluna que contém a data de nascimento identica ao do csv (formato Mês/Dia/Ano)
birthAgeDate = 'buyer_birth_date'

#nova coluna que será criada com a idade media calculada
idadeEmAnos = 'Idade Média'


#processamento de Múltiplos Arquivos (Consolidação)
allDateProcessed = []

print(f"Procurando arquivos: {raw_data}")

if not os.path.isdir(raw_data):
    print(f"Erro: A pasta '{raw_data}' não foi encontrada. Verifique o caminho.")
else:
    for arquivoCSV in os.listdir(raw_data):
        lendoColunas = os.path.join(raw_data, arquivoCSV)
        if os.path.isfile(lendoColunas) and arquivoCSV.endswith('.csv'):
            print(f"Lendo arquivo: {arquivoCSV}")
            try:
                #lendo a coluna de data de nascimento como data
                # dayfirst=False é crucial para o formato M/D/Y.
                df = pd.read_csv(lendoColunas, parse_dates=[birthAgeDate], dayfirst=False)
                allDateProcessed.append(df)
            except Exception as e:
                print(f"Erro ao ler ou processar data no arquivo {arquivoCSV}: {e}")


#gerar e analisar com cálculo de idade
if not allDateProcessed:
    print("Nenhum arquivo CSV encontrado.")
else:
    gerDados = pd.concat(allDateProcessed, ignore_index=True)
    print("\nGerando dados para análise.")

    #verificando se as colunas necessárias existem no DataFrame consolidado
    if countryColum not in gerDados.columns:
         print(f"Erro: A coluna '{countryColum}' não foi encontrada.")
    elif productSoldColum not in gerDados.columns:
        print(f"\nErro: A coluna '{productSoldColum}' não foi encontrada.")
    elif birthAgeDate not in gerDados.columns:
        print(f"\nErro: A coluna '{birthAgeDate}' não foi encontrada.")
    else:
        print("\nRealizando análise de idade média por país e produto...")

        #pegaando a data atual
        data_atual = pd.Timestamp(date.today())

        #Calcular a idade em anos
        #a diferença entre as datas resulta em Timedelta, dividido pelo número de dias em um ano.
        #.dt.days extrai a diferença em dias / 365.25 considera anos bissextos na média
        gerDados[idadeEmAnos] = (data_atual - gerDados[birthAgeDate]).dt.days / 365.25

        #arredondar para o ano completo para a idade
        gerDados[idadeEmAnos] = gerDados[idadeEmAnos].astype(int)

        #agrupamento e a média
        idadeMedia = gerDados.groupby([countryColum, productSoldColum])[idadeEmAnos].mean().reset_index()

        #ordenando os dados
        idadeMedia = idadeMedia.sort_values(by=[countryColum, idadeEmAnos], ascending=[True, False])

        #Resultado
        print("\nIdade Média por País e Produto")
        #Formatando a idade média calculada para ter 2 casas decimais
        idadeMedia[idadeEmAnos] = idadeMedia[idadeEmAnos].round(2)
        print(idadeMedia)