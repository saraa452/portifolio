import pandas as pd
import numpy as np
import os

# Caminho para a pasta de dados
caminho_dados = r'E:\Portifólio\portifolio\dados'

# Função para carregar e processar cada arquivo CSV
def processar_arquivo(nome_arquivo):
    try:
        # Carregar o arquivo CSV
        caminho_arquivo = os.path.join(caminho_dados, nome_arquivo)
        if not os.path.exists(caminho_arquivo):
            print(f"Arquivo {nome_arquivo} não encontrado! Pulando...")
            return
        
        df = pd.read_csv(caminho_arquivo, sep=';')

        print(f"\nProcessando {nome_arquivo}...")
        print("Resumo inicial:")
        print(df.info())

        # 1. Tratar dados faltantes
        # Preencher colunas numéricas com a média
        for coluna in df.select_dtypes(include=['float64', 'int64']).columns:
            if df[coluna].isnull().any():
                df[coluna].fillna(df[coluna].mean(), inplace=True)

        # Preencher colunas categóricas com o valor mais frequente
        for coluna in df.select_dtypes(include=['object']).columns:
            if df[coluna].isnull().any():
                df[coluna].fillna(df[coluna].mode()[0], inplace=True)

        # 2. Remover duplicatas
        duplicatas_antes = df.duplicated().sum()
        if duplicatas_antes > 0:
            df.drop_duplicates(inplace=True)
            print(f"Removidas {duplicatas_antes} duplicatas.")

        # 3. Conversão de tipos de dados
        # Converter colunas de data para o tipo datetime
        if 'Data' in df.columns:
            df['Data'] = pd.to_datetime(df['Data'], errors='coerce')

        # 4. Normalização (Min-Max Scaling) para colunas numéricas
        num_cols = df.select_dtypes(include=['float64', 'int64']).columns
        if not num_cols.empty:
            df[num_cols] = (df[num_cols] - df[num_cols].min()) / (df[num_cols].max() - df[num_cols].min())

        # 5. Remover outliers usando o método IQR
        for coluna in num_cols:
            Q1 = df[coluna].quantile(0.25)
            Q3 = df[coluna].quantile(0.75)
            IQR = Q3 - Q1
            limite_inferior = Q1 - 1.5 * IQR
            limite_superior = Q3 + 1.5 * IQR
            outliers_antes = df[(df[coluna] < limite_inferior) | (df[coluna] > limite_superior)].shape[0]
            df = df[(df[coluna] >= limite_inferior) & (df[coluna] <= limite_superior)]
            if outliers_antes > 0:
                print(f"Removidos {outliers_antes} outliers na coluna {coluna}.")

        # 6. Salvar o DataFrame processado
        caminho_saida = os.path.join(caminho_dados, f'processado_{nome_arquivo}')
        df.to_csv(caminho_saida, sep=';', index=False)
        print(f"Arquivo processado salvo como '{caminho_saida}'.")

    except Exception as e:
        print(f"Erro ao processar o arquivo {nome_arquivo}: {e}")

# Lista de arquivos CSV a serem processados
arquivos = ['clientes.csv', 'demanda.csv', 'vendas.csv']

# Processar cada arquivo
for arquivo in arquivos:
    processar_arquivo(arquivo)

print("\nProcessamento concluído!")
