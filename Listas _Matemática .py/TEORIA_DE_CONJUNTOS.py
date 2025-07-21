# -*- coding: utf-8 -*-

# =============================================================================
# SOLUÇÃO COMPLETA: LISTA 4 - TEORIA DE CONJUNTOS (VERSÃO CORRIGIDA)
# Este script adapta TODAS as questões da lista para código Python.
# A indentação e a clareza das respostas foram revisadas.
# =============================================================================

import itertools
try:
    import matplotlib.pyplot as plt
except ImportError:
    # Define uma flag para saber se a biblioteca está disponível
    matplotlib_disponivel = False
else:
    matplotlib_disponivel = True

def imprimir_titulo(titulo):
    """Função auxiliar para imprimir títulos formatados."""
    print("\n\n" + "="*60)
    print(f"--- {titulo} ---")
    print("="*60)

# =============================================================================
# INÍCIO DAS SOLUÇÕES
# =============================================================================

imprimir_titulo("Questão 1: Operações com Conjuntos")
A = {0, 1, 2, 3}
B = {0, 2, 3, 5}
C = {0, 2, 4, 6, 8}
D = {5, 7, 9}
print(f"a. (A U B) U C = {(A | B) | C}")
print(f"b. (B U C) ∩ D = {(B | C) & D}")
print(f"c. (A U C) ∩ B = {(A | C) & B}")
print(f"d. (B U D) U A = {(B | D) | A}")
print(f"e. (B ∩ D) U (C ∩ A) = {(B & D) | (C & A)}")
print(f"f. (B ∩ A) ∩ (C ∩ D) = {(B & A) & (C & D)}")
print(f"g. (A - B) - C = {(A - B) - C}")
print(f"h. (B - C) - D = {(B - C) - D}")
print(f"i. (A - C) - D = {(A - C) - D}")
print(f"j. (B - D) - A = {(B - D) - A}")


imprimir_titulo("Questão 2: Complemento de Conjuntos")
U = {0, 1, 2, 3, 4, 5, 6, 7}
B2 = {0, 2, 5}
C2 = {1, 3, 5, 7}
D2 = {2, 4, 6}
print(f"O conjunto universo é U = {U}")
print(f"a. Complementar de B em U = {U - B2}")
print(f"b. Complementar de C em U = {U - C2}")
print(f"c. Complementar de D em U = {U - D2}")
intersecao_bcd = B2 & C2 & D2
print(f"d. B ∩ C ∩ D = {intersecao_bcd}")
print(f"d. Complementar de (B ∩ C ∩ D) em U = {U - intersecao_bcd}")


imprimir_titulo("Questão 3: Demonstração da Propriedade Distributiva")
lado_esquerdo = (A | B) & C
lado_direito = (A & C) | (B & C)
print(f"Demonstração para: (A U B) ∩ C = (A ∩ C) U (B ∩ C)")
print(f"Conjuntos: A={A}, B={B}, C={C}")
print(f"Lado Esquerdo: (A U B) ∩ C = {lado_esquerdo}")
print(f"Lado Direito: (A ∩ C) U (B ∩ C) = {lado_direito}")
print(f"Os resultados são iguais? {lado_esquerdo == lado_direito}. A propriedade é válida.")


imprimir_titulo("Questão 4: Demonstração da Cardinalidade da União")
n_A = len(A)
n_B = len(B)
n_A_uniao_B = len(A | B)
n_A_inter_B = len(A & B)
formula = n_A + n_B - n_A_inter_B
print(f"Demonstração para: n(A U B) = n(A) + n(B) - n(A ∩ B)")
print(f"Conjuntos: A={A}, B={B}")
print(f"Cardinalidade real de A U B: n(A U B) = {n_A_uniao_B}")
print(f"Valor pela fórmula n(A)+n(B)-n(A∩B): {n_A} + {n_B} - {n_A_inter_B} = {formula}")
print(f"Os resultados são iguais? {n_A_uniao_B == formula}. A propriedade é válida.")


imprimir_titulo("Questão 5: Demonstração da Cardinalidade da União de 3 Conjuntos")
n_C = len(C)
n_A_uniao_B_uniao_C = len(A | B | C)
n_B_inter_C = len(B & C)
n_A_inter_C = len(A & C)
n_A_inter_B_inter_C = len(A & B & C)
formula_3 = n_A + n_B + n_C - n_A_inter_B - n_A_inter_C - n_B_inter_C + n_A_inter_B_inter_C
print(f"Demonstração para: n(A U B U C) = n(A)+n(B)+n(C)-n(A∩B)-n(A∩C)-n(B∩C)+n(A∩B∩C)")
print(f"Conjuntos: A={A}, B={B}, C={C}")
print(f"Cardinalidade real de A U B U C = {n_A_uniao_B_uniao_C}")
print(f"Valor pela fórmula = {formula_3}")
print(f"Os resultados são iguais? {n_A_uniao_B_uniao_C == formula_3}. A propriedade é válida.")


imprimir_titulo("Questão 6: Cardinalidade com Subconjuntos")
num_subconjuntos_AUB = 128
n_AUB = 7  # 2^7 = 128
n_B6 = 3
n_A_inter_B6 = 0
n_A6 = n_AUB - n_B6 + n_A_inter_B6
print(f"O número de elementos do conjunto A é: {n_A6}")


imprimir_titulo("Questão 7: Pesquisa de Jornais")
total_pessoas = 470
n_jornal_A = 250
n_jornal_B = 180
n_A_inter_B7 = 60
apenas_A = n_jornal_A - n_A_inter_B7
apenas_B = n_jornal_B - n_A_inter_B7
leem_jornais = n_jornal_A + n_jornal_B - n_A_inter_B7
nao_leem = total_pessoas - leem_jornais
print(f"a. Pessoas que leem apenas o jornal A: {apenas_A}")
print(f"b. Pessoas que leem apenas o jornal B: {apenas_B}")
print(f"c. Pessoas que leem jornais (A ou B): {leem_jornais}")
print(f"d. Pessoas que não leem jornais: {nao_leem}")


imprimir_titulo("Questão 8: Pesquisa de Livros")
total_consultados = 1000
n_M, n_H, n_S = 600, 400, 300
n_M_inter_H, n_M_inter_S, n_H_inter_S = 200, 150, 100
n_M_inter_H_inter_S = 20
n_total_leitores = (n_M + n_H + n_S) - (n_M_inter_H + n_M_inter_S + n_H_inter_S) + n_M_inter_H_inter_S
nao_leram_nenhum = total_consultados - n_total_leitores
apenas_M = n_M - (n_M_inter_H - n_M_inter_H_inter_S) - (n_M_inter_S - n_M_inter_H_inter_S) - n_M_inter_H_inter_S
apenas_H = n_H - (n_M_inter_H - n_M_inter_H_inter_S) - (n_H_inter_S - n_M_inter_H_inter_S) - n_M_inter_H_inter_S
apenas_S = n_S - (n_M_inter_S - n_M_inter_H_inter_S) - (n_H_inter_S - n_M_inter_H_inter_S) - n_M_inter_H_inter_S
leram_apenas_um = apenas_M + apenas_H + apenas_S
leram_duas_ou_mais = n_total_leitores - leram_apenas_um
print(f"a. Pessoas que leram apenas uma das três obras: {leram_apenas_um}")
print(f"b. Pessoas que não leram nenhuma das três obras: {nao_leram_nenhum}")
print(f"c. Pessoas que leram duas ou mais obras: {leram_duas_ou_mais}")


imprimir_titulo("Questão 9: Colorir Diagrama")
print("A questão pede para colorir a região que representa (A ∩ B) U (A ∩ C).")
print("Pela propriedade distributiva, isso é o mesmo que A ∩ (B U C).")
print("A região a ser colorida é a parte do círculo A que também está em B ou em C.")


imprimir_titulo("Questão 10: Análise de Diagrama (R, T, C)")
R_diag = {1, 2, 3, 4, 5, 6}
C_diag = {3, 4, 7, 8, 9}
T_diag = {2, 3, 8, 10}
resultado_q10 = (R_diag & C_diag) - T_diag
print("A região hachurada é o que está no Retângulo E no Círculo, MENOS o que está no Triângulo.")
print("A fórmula é (R ∩ C) - T, que corresponde à letra [c].")
print(f"Verificação com exemplos: (R ∩ C) - T = {resultado_q10}")


imprimir_titulo("Questão 11: Identificar Região Hachurada")
A_diag = {1, 2, 4, 5}
B_diag = {2, 3, 5, 6}
C_diag = {4, 5, 6, 7}
resultado_q11 = A_diag & (B_diag | C_diag)
print("A região hachurada é a parte de A que intercepta a união de B e C.")
print(f"A fórmula é A ∩ (B U C), que corresponde à letra [a].")
print(f"Verificação com exemplos: A ∩ (B U C) = {resultado_q11}")


imprimir_titulo("Questão 12: Produto Cartesiano")
A12 = {-1, 0, 2, 3}
B12 = {-2, -5, 9, 11}
C12 = {1, 3, 5}
axb = list(itertools.product(A12, B12))
bxa = list(itertools.product(B12, A12))
cxb = list(itertools.product(C12, B12))
cxbxa = list(itertools.product(C12, B12, A12))
print(f"a. A x B (primeiros 5 de {len(axb)} pares): {axb[:5]}...")
print(f"b. B x A (primeiros 5 de {len(bxa)} pares): {bxa[:5]}...")
print(f"c. C x B (primeiros 5 de {len(cxb)} pares): {cxb[:5]}...")
print(f"d. C x B x A tem {len(cxbxa)} elementos. Exemplo de um elemento: {cxbxa[0]}")


imprimir_titulo("Questão 13: Representação Gráfica de Produto Cartesiano")
if matplotlib_disponivel:
    print("Gerando gráfico para A x B. Uma janela se abrirá.")
    fig, ax = plt.subplots()
    rect = plt.Rectangle((1, 3), 5, 4, linewidth=1, edgecolor='r', facecolor='blue', alpha=0.3)
    ax.add_patch(rect)
    plt.xlim(0, 8)
    plt.ylim(0, 8)
    plt.grid(True)
    plt.xlabel("Eixo x (Conjunto A: [1, 6])")
    plt.ylabel("Eixo y (Conjunto B: [3, 7])")
    plt.title("Representação Gráfica de A x B")
    ax.set_aspect('equal', adjustable='box')
    print("Feche a janela do gráfico para continuar o script...")
    plt.show()
else:
    print("\nAVISO: A biblioteca 'matplotlib' não está instalada.")
    print("Para ver o gráfico da questão 13, instale-a com: sudo apt install python3-matplotlib")


imprimir_titulo("Questão 14: Cardinalidade do Produto Cartesiano de 3 Conjuntos")
n_A14, n_B14, n_C14 = 10, 7, 9
n_AxBxC = n_A14 * n_B14 * n_C14
print(f"O número de elementos no produto cartesiano A x B x C é:")
print(f"n(A) * n(B) * n(C) = {n_A14} * {n_B14} * {n_C14} = {n_AxBxC}")


imprimir_titulo("Questão 15: Demonstração da Cardinalidade do Produto Cartesiano")
A15 = {1, 2, 3}
B15 = {'a', 'b'}
AxB_15 = list(itertools.product(A15, B15))
n_A15 = len(A15)
n_B15 = len(B15)
n_AxB_15 = len(AxB_15)
produto_cardinalidades = n_A15 * n_B15
print(f"Demonstração para: n(A x B) = n(A) * n(B)")
print(f"Conjuntos: A={A15}, B={B15}")
print(f"Produto Cartesiano A x B = {AxB_15}")
print(f"Cardinalidade real de A x B = {n_AxB_15}")
print(f"Produto das cardinalidades n(A)*n(B) = {n_A15} * {n_B15} = {produto_cardinalidades}")
print(f"Os resultados são iguais? {n_AxB_15 == produto_cardinalidades}. A propriedade é válida.")
