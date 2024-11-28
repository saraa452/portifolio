import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Definir o caminho para a pasta de resultados
resultados_path = r'E:\Portifólio\portifolio\resultados\análise_sentimentos'

# Verificar se a pasta existe, caso contrário, criar a pasta
if not os.path.exists(resultados_path):
    os.makedirs(resultados_path)

# Carregar o arquivo CSV
df_sentimentos = pd.read_csv(r'E:\Portifólio\portifolio\dados\sentimentos.csv', sep=',')

# Configurações iniciais
sns.set_theme(style='darkgrid', palette='viridis')

# 1. Visão Geral dos Dados
print("Resumo Estatístico:")
print(df_sentimentos.describe(include='all'))
print("\nInformações do DataFrame:")
print(df_sentimentos.info())

# Verificação das colunas esperadas
required_columns = ['Texto']
if 'Texto' not in df_sentimentos.columns:
    print("Coluna 'Texto' não encontrada no DataFrame. Verifique o arquivo de entrada.")
    exit()

# 2. Função para calcular o sentimento
def analise_sentimento(texto):
    return TextBlob(texto).sentiment.polarity

# 3. Aplicar análise de sentimentos
df_sentimentos['Sentimento'] = df_sentimentos['Texto'].apply(analise_sentimento)

# 4. Classificar sentimentos
df_sentimentos['Classificacao'] = df_sentimentos['Sentimento'].apply(
    lambda x: 'Positivo' if x > 0 else ('Negativo' if x < 0 else 'Neutro')
)

# 5. Visualizar a distribuição dos sentimentos
plt.figure(figsize=(8, 6))
sns.countplot(data=df_sentimentos, x='Classificacao', palette='pastel', order=['Positivo', 'Neutro', 'Negativo'])
plt.title('Distribuição dos Sentimentos')
plt.xlabel('Classificação')
plt.ylabel('Frequência')
plt.tight_layout()
# Salvar o gráfico na pasta de resultados
plt.savefig(os.path.join(resultados_path, 'distribuicao_sentimentos.png'))
plt.show()

# 6. Exportar resultados para arquivo CSV
output_csv_path = os.path.join(resultados_path, 'resultados_sentimentos.csv')
df_sentimentos.to_csv(output_csv_path, sep=';', index=False)
print(f"Resultados exportados para '{output_csv_path}'.")
