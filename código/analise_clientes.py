import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Definir o caminho para a pasta de resultados
resultados_path = r'E:\Portifólio\portifolio\resultados\análise_clientes'

# Verificar se a pasta existe, caso contrário, criar a pasta
if not os.path.exists(resultados_path):
    os.makedirs(resultados_path)

# Carregar o arquivo CSV
df_clientes = pd.read_csv(r'E:\Portifólio\portifolio\dados\processado_clientes.csv', sep=',')

# Verificação das colunas esperadas
required_columns = ['Idade', 'Genero', 'Status_Fidelidade']
for col in required_columns:
    if col not in df_clientes.columns:
        print(f"Coluna '{col}' não encontrada no DataFrame.")
        exit()

# Configurações iniciais
sns.set_theme(style='darkgrid', palette='viridis')

# 1. Visão Geral dos Dados
print("Resumo Estatístico:")
print(df_clientes.describe(include='all'))
print("\nInformações do DataFrame:")
print(df_clientes.info())

# 2. Análise da Distribuição de Idade
plt.figure(figsize=(10, 6))
sns.histplot(df_clientes['Idade'], bins=30, kde=True)
plt.title('Distribuição de Idade dos Clientes')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.tight_layout()
# Salvar o gráfico na pasta de resultados
plt.savefig(os.path.join(resultados_path, 'distribuicao_idade.png'))
plt.show()

# 3. Análise de Gênero
plt.figure(figsize=(8, 6))
sns.countplot(data=df_clientes, x='Genero', palette='pastel')
plt.title('Distribuição de Gênero dos Clientes')
plt.xlabel('Gênero')
plt.ylabel('Frequência')
plt.tight_layout()
# Salvar o gráfico na pasta de resultados
plt.savefig(os.path.join(resultados_path, 'distribuicao_genero.png'))
plt.show()

# 4. Análise de Status de Fidelidade
plt.figure(figsize=(10, 6))
sns.countplot(data=df_clientes, x='Status_Fidelidade', palette='muted')
plt.title('Distribuição de Status de Fidelidade dos Clientes')
plt.xlabel('Status de Fidelidade')
plt.ylabel('Frequência')
plt.tight_layout()
# Salvar o gráfico na pasta de resultados
plt.savefig(os.path.join(resultados_path, 'status_fidelidade.png'))
plt.show()

# 5. Exportar resumo para arquivo CSV
resumo_clientes = df_clientes.groupby('Genero')['Idade'].describe()
# Salvar o resumo na pasta de resultados
resumo_clientes.to_csv(os.path.join(resultados_path, 'resumo_comportamento_clientes.csv'), sep=';')
print("Resumo exportado para 'resultados/análise_clientes/resumo_comportamento_clientes.csv'.")

