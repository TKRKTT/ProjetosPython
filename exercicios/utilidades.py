def saudar(nome_da_pessoa):
    """
    Esta função inprime uma saudação personaliarda.
    Recebe um nome como parãmento e retorna uma string formada.
    """
    print(f"Olá, {nome_da_pessoa}! Seja bem-vindo(a)!")

def calcular_dobro(numero):
    """
    Esta funçãp calcular o drobro de um número.
    Recebe um argumento: numero (numérico).
    Retona: o drobo do número.
    """
    drobro = numero * 2
    return drobro # 'return' envia o valor de volta para quem chamou a função

def verificar_par_ou_impar(valor):
    """
    Esta função verifica se um número é par ou ímpar.
    Recebe um argumento: valor (numérico inteiro).
    """
    if valor % 2 == 0: # O oprador '%'(módulo) retona o resto da divisão
        print(f" O número {valor} é par.")
    else:
        print(f"O número {valor} é impar.")

def exibir_lista_com_indices(lista):
    """
    Esta função exibe os elementos de uma lista com seus respectivos índices.
    Recebe um argumento: lista (qualquer lista).

    """
    print("\n --- Itens da Lista com Índices ---")
    for indice, item in enumerate(lista):
        print(f"[{indice}]: {item}")

# Fim de utilidades.pay