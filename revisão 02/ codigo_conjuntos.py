# codigo_conjuntos.py

def calcular_produto_cartesiano(vetor1, nome_vetor1, vetor2, nome_vetor2):
    """
    Calcula o produto cartesiano entre dois vetores (listas).
    Isso é uma ótima prática para o uso de Funções e Matrizes.
    """
    print(f"\n--- Calculando o Produto Cartesiano: {nome_vetor1} x {nome_vetor2} ---")
    
    # A matriz resultado será uma lista de listas (ou tuplas)
    matriz_resultado = []
    
    # Usando laços aninhados para criar os pares ordenados
    for elemento1 in vetor1:
        for elemento2 in vetor2:
            par_ordenado = (elemento1, elemento2)
            matriz_resultado.append(par_ordenado)
            
    return matriz_resultado

def calcular_cardinalidade_produto_triplo(vetor1, vetor2, vetor3):
    """
    Calcula o número de elementos do produto cartesiano de 3 conjuntos.
    """
    # n(A x B x C) = n(A) * n(B) * n(C)
    return len(vetor1) * len(vetor2) * len(vetor3)

# --- Programa Principal ---

# 1. Representando os conjuntos como vetores (listas em Python) [cite: 8]
A = [-1, 0, 2, 3]
B = [-2, -5, 9, 11]
C = [1, 3, 5]

print("Conjuntos Originais:")
print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")

# 2. Calculando e exibindo A x B [cite: 9]
produto_A_x_B = calcular_produto_cartesiano(A, "A", B, "B")
print("Resultado de A x B (os pares são os elementos da matriz):")
print(produto_A_x_B)

# 3. Calculando e exibindo B x C [cite: 9]
produto_B_x_C = calcular_produto_cartesiano(B, "B", C, "C")
print("Resultado de B x C:")
print(produto_B_x_C)

# 4. Calculando n(A x B x C) [cite: 11]
cardinalidade = calcular_cardinalidade_produto_triplo(A, B, C)
print(f"\n--- Calculando a Cardinalidade n(A x B x C) ---")
print(f"O número de elementos em A x B x C é: {cardinalidade}")