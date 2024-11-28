import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Definir o caminho para a pasta de resultados
resultados_path = r'E:\Portifólio\portifolio\resultados\analise_demanda'

# Verificar se a pasta existe, caso contrário, criar a pasta
if not os.path.exists(resultados_path):
    os.makedirs(resultados_path)

# Carregar o arquivo CSV
df_demanda = pd.read_csv(r'E:\Portifólio\portifolio\dados\processado_demanda.csv')

# Verificação das colunas esperadas
required_columns = ['Data', 'Produto', 'Quantidade']
for col in required_columns:
    if col not in df_demanda.columns:
        print(f"Coluna '{col}' não encontrada no DataFrame.")
        exit()

# Configurações iniciais
sns.set_theme(style='darkgrid', palette='viridis')

# 1. Visão Geral dos Dados
print("Resumo Estatístico:")
print(df_demanda.describe(include='all'))
print("\nInformações do DataFrame:")
print(df_demanda.info())

# 2. Análise da Evolução da Demanda ao Longo do Tempo
# Converter a coluna Data para datetime
df_demanda['Data'] = pd.to_datetime(df_demanda['Data'], errors='coerce')

# Remover linhas com valores inválidos na coluna Data
if df_demanda['Data'].isna().sum() > 0:
    print("Linhas com datas inválidas foram removidas.")
    df_demanda = df_demanda.dropna(subset=['Data'])

demanda_por_data = df_demanda.groupby('Data')['Quantidade'].sum()

plt.figure(figsize=(12, 6))
demanda_por_data.plot(marker='o', linestyle='-', color='blue')
plt.title('Evolução da Demanda ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Quantidade Demandada')
plt.grid(True)
plt.tight_layout()
# Salvar o gráfico na pasta de resultados
plt.savefig(os.path.join(resultados_path, 'evolucao_demanda.png'))
plt.show()

# 3. Análise da Distribuição da Demanda por Produto
plt.figure(figsize=(10, 6))
sns.barplot(data=df_demanda, x='Produto', y='Quantidade', palette='pastel', ci=None)
plt.title('Distribuição da Demanda por Produto')
plt.xlabel('Produto')
plt.ylabel('Quantidade Total')
plt.xticks(rotation=45)
plt.tight_layout()
# Salvar o gráfico na pasta de resultados
plt.savefig(os.path.join(resultados_path, 'distribuicao_produto.png'))
plt.show()

# 4. Análise de Picos de Demanda
picos_demanda = demanda_por_data[demanda_por_data > demanda_por_data.mean() + 2 * demanda_por_data.std()]

plt.figure(figsize=(12, 6))
plt.plot(demanda_por_data.index, demanda_por_data, label='Demanda', color='blue')
plt.scatter(picos_demanda.index, picos_demanda, color='red', label='Picos de Demanda')
plt.title('Picos de Demanda Identificados')
plt.xlabel('Data')
plt.ylabel('Quantidade Demandada')
plt.legend()
plt.grid(True)
plt.tight_layout()
# Salvar o gráfico na pasta de resultados
plt.savefig(os.path.join(resultados_path, 'picos_demanda.png'))
plt.show()

# 5. Exportar resumo para arquivo CSV
resumo_demanda = df_demanda.groupby('Produto')['Quantidade'].sum().reset_index()
# Salvar o resumo na pasta de resultados com o nome ajustado
resumo_demanda.to_csv(os.path.join(resultados_path, 'resumo_demanda.csv'), sep=';')
print(f"Resumo exportado para '{os.path.join(resultados_path, 'resumo_demanda.csv')}'.")
