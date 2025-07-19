# Questão04.py - Função para Calcular Média

# 1. Crie uma função chamada calcular_media
def calcular_media(lista_de_numeros): # Renomeei o parâmetro para 'lista_de_numeros' para clareza
    """
    Esta função calcula a média de uma lista de números.
    Recebe: uma lista de números (list).
    Retorna: a média dos números (float).
    """
    # Verifica se a lista não está vazia para evitar divisão por zero
    if not lista_de_numeros:
        return 0.0 # Retorna 0.0 se a lista estiver vazia para evitar erro
    
    soma = sum(lista_de_numeros) # Calcula a soma de todos os números na lista
    quantidade = len(lista_de_numeros) # Conta quantos números há na lista
    
    media = soma / quantidade # Calcula a média
    return media # Corrigido 'retun' para 'return' e retorna o valor calculado

# Lista de valores para testar a função
valores = [10, 20, 30, 40, 50]

# Chamando a função com a lista 'valores' e imprimindo o resultado
# Usando f-string para formatar a saída corretamente
media_calculada = calcular_media(valores) # Armazena o resultado da função em uma variável
print(f"A média dos números {valores} é {media_calculada}.") # Exibe a lista original e a média
