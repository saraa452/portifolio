E:\
└── Portifólio\
    └── portifolio\
        ├── dados\
        │   ├── clientes.csv
        │   ├── demanda.csv
        │   ├── sentimentos.csv
        │   ├── processado_clientes.csv
        │   ├── processado_demanda.csv
        │   └── processado_sentimentos.csv
        ├── código\
        │   ├── analise_clientes.py
        │   ├── previsao_demanda.py
        │   ├── analise_sentimentos.py
        │   ├── modelagem_vendas.py
        │   └── processamento.py
        ├── resultados\
        │   ├── analise_clientes\
        │   ├── previsao_demanda\
        │   └── analise_sentimentos\
        ├── index.html
        └── README.md
Arquivos
Dados Brutos:
clientes.csv: Contém informações demográficas e comportamentais dos clientes.
demanda.csv: Dados históricos de demanda de produtos ou serviços.
sentimentos.csv: Feedbacks/opiniões usados para análise de sentimento.
Dados Processados:
Arquivos com prefixo processado_ são os resultados do pré-processamento (limpeza, normalização, etc.).
Análises Realizadas
1. Análise de Sentimentos
No arquivo sentimentos.csv, utilizamos a biblioteca TextBlob para calcular a polaridade e classificar os sentimentos em:

Positivo
Negativo
Neutro
2. Pré-processamento de Dados
As etapas de pré-processamento incluem:

Tratamento de Dados Faltantes
Colunas numéricas: Substituição de valores ausentes pela média.
Colunas categóricas: Preenchimento com a moda.
Remoção de Duplicatas
Exclusão de registros duplicados para evitar redundâncias.
Conversão de Tipos
Colunas de data convertidas para o formato datetime.
Normalização
Aplicação do método Min-Max Scaling para padronizar os valores numéricos entre 0 e 1.
Remoção de Outliers
Utilização do Intervalo Interquartil (IQR) para identificar e remover valores extremos.
Como Executar o Projeto
Clone o repositório:

bash
Copiar código
git clone <URL_DO_REPOSITORIO>
Instale as dependências: Certifique-se de que as bibliotecas necessárias estão instaladas:

bash
Copiar código
pip install pandas numpy textblob matplotlib seaborn
Execute o script de pré-processamento: Navegue até o diretório código e execute:

bash
Copiar código
python processamento.py
Resultados
Os resultados são organizados da seguinte forma:

Arquivos processados são salvos na pasta dados/ com o prefixo processado_.
Gráficos e relatórios são armazenados na pasta resultados/.
Esses dados e análises estão prontos para serem utilizados em tarefas adicionais, como previsão de demanda ou modelagem de vendas.

Contribuições
Sinta-se à vontade para:

Relatar problemas (issues).
Sugerir melhorias.
Contribuir com novos scripts ou análises.
Licença
Este projeto está licenciado sob a MIT License. Sinta-se livre para utilizá-lo, modificar ou distribuir com os devidos créditos.

