# utilidades.py - Este arquivo vai conter funções úteis

def saudar(nome_da_pessoa):
    """
    Esta função imprime uma saudação personalizada. # 'inprime' e 'personaliarda' corrigidos
    Recebe um nome como parâmetro e retorna uma string formada. # 'parãmento' corrigido
    """
    print(f"Olá, {nome_da_pessoa}! Seja bem-vindo(a)!")

def calcular_dobro(numero):
    """
    Esta função calcula o dobro de um número. # 'funçãp' e 'drobro' corrigidos
    Recebe um argumento: numero (numérico).
    Retorna: o dobro do número. # 'Retona' e 'drobo' corrigidos
    """
    dobro = numero * 2
    return dobro # 'return' envia o valor de volta para quem chamou a função

def verificar_par_ou_impar(valor):
    """
    Esta função verifica se um número é par ou ímpar.
    Recebe um argumento: valor (numérico inteiro).
    """
    if valor % 2 == 0: # O operador '%' (módulo) retorna o resto da divisão # 'oprador' e 'retona' corrigidos
        print(f" O número {valor} é par.")
    else:
        print(f"O número {valor} é ímpar.") # 'impar' corrigido

def exibir_lista_com_indices(lista):
    """
    Esta função exibe os elementos de uma lista com seus respectivos índices.
    Recebe um argumento: lista (qualquer lista).

    """
    print("\n --- Itens da Lista com Índices ---")
    for indice, item in enumerate(lista):
        print(f"[{indice}]: {item}")

# Fim de utilidades.py # 'utilidades.pay' corrigido
