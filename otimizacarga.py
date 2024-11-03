import streamlit as st
import pandas as pd
from geneticalgorithm import geneticalgorithm as ga

# Configuração da página do Streamlit
st.set_page_config(page_title="Otimização de Transporte de Carga", layout="wide")
st.title("Otimização de Transporte de Carga")

# Função para carregar dados de um arquivo CSV
def carregar_dados(file):
    dados = pd.read_csv(file, sep=";")  # Carrega o CSV
    expected_columns = {'PESO', 'VOLUME', 'VALOR'}  # Colunas esperadas no arquivo
    if not expected_columns.issubset(dados.columns):  # Verifica se as colunas estão presentes
        st.error("O arquivo CSV deve conter as colunas: PESO, VOLUME e VALOR.")
        return None
    return dados  # Retorna os dados carregados

# Função que calcula a aptidão (fitness) de uma solução
def fitness_function(X, data, max_volume, max_weight):
    itens_selecionados = data.iloc[X.astype(bool),:]  # Seleciona itens com base na solução binária
    peso_total = itens_selecionados['PESO'].sum()  # Calcula o peso total dos itens selecionados
    volume_total = itens_selecionados['VOLUME'].sum()  # Calcula o volume total dos itens selecionados
    # Verifica se os limites de peso e volume são respeitados
    if peso_total > max_weight or volume_total > max_volume:
        return -1  # Penaliza soluções que excedem os limites
    else:
        return -itens_selecionados['VALOR'].sum()  # Retorna o valor negativo total para maximização

dados = None  # Inicializa a variável de dados

# Cria duas colunas para layout
col1, col2 = st.columns(2)

# Seção para upload de dados
with col1.expander("Dados"):
    arquivo = st.file_uploader("Selecione o arquivo", type='csv')  # Permite o upload de um arquivo CSV
    if arquivo is not None:
        dados = carregar_dados(arquivo)  # Carrega os dados do arquivo
        botao_calcular_totais = st.button("Calcular Totais")  # Botão para calcular totais
        if botao_calcular_totais:
            # Exibe os dados e estatísticas
            st.write(dados)
            st.write(f"Quantidade de Itens: {len(dados)} ")
            st.write(f"Peso Total: {dados['PESO'].sum()} ")
            st.write(f"Volume Total: {dados['VOLUME'].sum()}")
            st.write(f"Valor Total: {dados['VALOR'].sum()}")

# Seção para processamento do algoritmo
with col2.expander("Processamento"):
    if dados is not None:  # Verifica se os dados foram carregados
        sobra_peso = st.number_input("Informa a sobra de Peso", value=6000, step=500)  # Input para peso disponível
        sobra_volume = st.number_input("Informe a sobra de Volume", value=350, step=100)  # Input para volume disponível
        iteracao = st.number_input("Informe a quantidade de Iterações", value=10, step=1)  # Input para número de iterações
        botao_processar = st.button("Processar")  # Botão para iniciar o processamento
        if botao_processar:
            # Define parâmetros do algoritmo genético
            parametros_algoritmo = {
                'max_num_iteration': iteracao,  # Número máximo de iterações
                'population_size': 10,  # Tamanho da população
                'mutation_probability': 0.1,  # Probabilidade de mutação
                'elit_ratio': 0.01,  # Porcentagem de elitismo
                'crossover_probability': 0.5,  # Probabilidade de cruzamento
                'parents_portion': 0.3,  # Porcentagem de pais na seleção
                'crossover_type': 'uniform',  # Tipo de cruzamento
                'max_iteration_without_improv': None  # Parar se não houver melhoria
            }
            varbound = [[0, 1]] * len(dados)  # Define os limites para as variáveis

            # Inicializa o modelo do algoritmo genético
            modelo = ga(
                function=lambda X: fitness_function(X, dados, sobra_volume, sobra_peso),  # Função de fitness
                dimension=len(dados),  # Número de itens
                variable_type='bool',  # Tipo de variável (bool)
                variable_boundaries=varbound,  # Limites das variáveis
                algorithm_parameters=parametros_algoritmo  # Parâmetros do algoritmo
            )
            modelo.run()  # Executa o algoritmo

            # Seleciona a melhor solução encontrada
            solucao = dados.iloc[modelo.output_dict['variable'].astype(bool), :]

            # Exibe os resultados
            st.write("Solução Otimizada:")
            st.write(solucao)
            st.write(f"Quantidade Final: {len(solucao)}")
            st.write(f"Peso Final: {solucao['PESO'].sum()}")
            st.write(f"Volume Final: {solucao['VOLUME'].sum()}")
            st.write(f"Valor Total: {solucao['VALOR'].sum()}")
