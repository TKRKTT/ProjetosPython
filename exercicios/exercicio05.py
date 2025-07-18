# exercicio05.py - Usando as funções do arquivo utilidades.py # 'arquvivo' corrigido

# 'from nome_do_arquivo import nome_da_funcao' # 'inport' e 'função'' corrigidos
from utilidades import saudar, calcular_dobro, verificar_par_ou_impar, exibir_lista_com_indices
print("---- Iniciando o exercício05.py ----")

# 1. Usando a função saudar
seu_nome = input("Digite seu nome:") # 'Dite' corrigido
saudar(seu_nome)

# 2. Usando a função calcular_dobro
numero_digitado = float(input("Digite um número para calcular o dobro:"))
resultado_dobro = calcular_dobro(numero_digitado)
print(f"O dobro de {numero_digitado} é {resultado_dobro}.") # 'drobro' corrigido

# 3. Usando a função verificar_par_ou_impar
num_para_verificar = int(input("Digite um número inteiro para verificar se é par ou ímpar:"))
verificar_par_ou_impar(num_para_verificar)

# 4. Usando a função exibir_lista_com_indices
lista_compras = ["arroz", "feijão", "macarrão", "carne", "frutas"] # Aspas adicionadas aos itens
exibir_lista_com_indices(lista_compras)

outras_listas_frutas = ["maçã", "banana", "laranja", "melão", "abacaxi"] # Aspas adicionadas aos itens
exibir_lista_com_indices(outras_listas_frutas)

print("---- Exercício com Funções finalizado ----")