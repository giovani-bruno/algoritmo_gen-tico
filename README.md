# Otimização de Transporte de Carga

## Descrição

Este projeto visa otimizar o transporte de carga de uma empresa aérea fictícia utilizando um Algoritmo Genético. O sistema permite que o usuário insira informações sobre itens a serem transportados e calcule a melhor combinação possível para maximizar o lucro, respeitando as restrições de peso e volume das aeronaves.

## Funcionalidades

- Carregamento de dados a partir de arquivos CSV personalizados.
- Cálculo de totais (peso, volume e valor) dos itens carregados.
- Otimização do transporte de carga usando um Algoritmo Genético.
- Seleção da combinação mais lucrativa de itens a serem transportados.
- Interface interativa construída com Streamlit.

## Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Genetic Algorithm](https://pypi.org/project/geneticalgorithm/)

## Como Usar

1. Clone o repositório:

   ```
   git clone https://github.com/giovani-burno/algoritmo_genetico.git
   ```
2. Navegue até o diretório do projeto:
   ```
   cd algoritmo_genetico
   ```
3. Instale as dependências necessárias:
   ```
   pip install -r requirements.txt
   ```
4. Execute a aplicação Steramlit:
   ```
   streamlit run otimizacarga.py
   ```
