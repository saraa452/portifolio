import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Definir o caminho para a pasta de resultados
resultados_path = r'E:\Portifólio\portifolio\resultados\modelagem_vendas'

# Carregar o arquivo CSV com o separador correto
df = pd.read_csv(r'E:\Portifólio\portifolio\dados\processado_vendas.csv', sep=';')

# Limpar os espaços em branco dos nomes das colunas
df.columns = df.columns.str.strip()

# Verificação se as colunas necessárias estão presentes
required_columns = ['Produto', 'Categoria', 'Valor_Total', 'Data_Venda', 'Forma_Pagamento']
for col in required_columns:
    if col not in df.columns:
        print(f"Coluna '{col}' não encontrada no DataFrame.")
        exit()

# Configurações iniciais
# Usar um estilo do seaborn diretamente
sns.set_theme(style="darkgrid")
sns.set_palette('viridis')


# 1. Visão Geral dos Dados
print("Resumo Estatístico:")
print(df.describe(include='all'))
print("\nInformações do DataFrame:")
print(df.info())

# 2. Análise de Vendas por Produto
vendas_por_produto = df.groupby('Produto')['Valor_Total'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
vendas_por_produto.plot(kind='bar', color='skyblue')
plt.title('Vendas Totais por Produtos')
plt.xlabel('Produtos')
plt.ylabel('Vendas Totais (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('vendas_por_produto.png')
plt.show()

# 3. Análise de Vendas por Categoria
vendas_por_categoria = df.groupby('Categoria')['Valor_Total'].sum()

plt.figure(figsize=(8, 6))
vendas_por_categoria.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#66c2a5', '#fc8d62'])
plt.title('Distribuição de Vendas por Categoria')
plt.ylabel('')
plt.tight_layout()
plt.savefig('vendas_por_categoria.png')
plt.show()

# 4. Análise Temporal de Vendas
# Converter a coluna Data_Venda para datetime
df['Data_Venda'] = pd.to_datetime(df['Data_Venda'], errors='coerce')  # Usar 'coerce' para lidar com erros de conversão

# Remover linhas com datas inválidas
df = df.dropna(subset=['Data_Venda'])

vendas_por_mes = df.groupby(df['Data_Venda'].dt.to_period('M'))['Valor_Total'].sum()

plt.figure(figsize=(12, 6))
vendas_por_mes.plot(marker='o', linestyle='-', color='purple')
plt.title('Evolução Mensal das Vendas')
plt.xlabel('Mês')
plt.ylabel('Vendas Totais (R$)')
plt.grid(True)
plt.tight_layout()
plt.savefig('evolucao_mensal_vendas.png')
plt.show()

# 5. Análise de Vendas por Forma de Pagamento
vendas_por_pagamento = df.groupby('Forma_Pagamento')['Valor_Total'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
vendas_por_pagamento.plot(kind='bar', color='#ff7f0e')
plt.title('Vendas Totais por Forma de Pagamento')
plt.xlabel('Forma de Pagamento')
plt.ylabel('Vendas Totais (R$)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('vendas_por_pagamento.png')
plt.show()

# 6. Exportar resumo para arquivo CSV
resumo = df.groupby('Produto')['Valor_Total'].sum().reset_index()
# Salvar o resumo na pasta de resultados
resumo.to_csv(os.path.join(resultados_path, 'resumo_comportamento_clientes.csv'), sep=';')
print("Resumo exportado para 'resultados/análise_clientes/resumo_comportamento_clientes.csv'.")

