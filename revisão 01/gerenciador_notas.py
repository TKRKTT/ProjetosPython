# gerenciador_notas.py - Módulo para a lógica de gerenciamento de notas

# Lista global para armazenar os dicionários de alunos
alunos = []

# --- Funções Auxiliares ---

def calcular_media(lista_de_numeros):
    """
    Calcula a média de uma lista de números.
    Recebe: uma lista de números (list).
    Retorna: a média dos números (float).
    """
    if not lista_de_numeros:
        return 0.0
    soma = sum(lista_de_numeros)
    quantidade = len(lista_de_numeros)
    return soma / quantidade

# --- Funções do Sistema de Notas ---