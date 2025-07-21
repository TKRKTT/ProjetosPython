# -*- coding: utf-8 -*-

# =============================================================================
# SOLUÇÃO: LISTA 5 - PRINCÍPIO DE INDUÇÃO FINITA (3 PRIMEIRAS QUESTÕES)
# Este script faz a verificação numérica para as 3 primeiras fórmulas
# da lista, conforme solicitado.
# =============================================================================

import math

def imprimir_titulo(titulo):
    """Função auxiliar para imprimir títulos formatados."""
    print("\n\n" + "="*60)
    print(f"--- {titulo} ---")
    print("="*60)

# =============================================================================
# INÍCIO DAS SOLUÇÕES
# =============================================================================

imprimir_titulo("Questão 1: Verificação Numérica de Provas por Indução")
n = 100  # Usaremos n=100 para verificar as fórmulas

# --- a. Soma dos n primeiros inteiros ---
# Provar que 1+2+...+n = n(n+1)/2
print("\n--- a. Soma dos n primeiros inteiros ---")
soma_real_a = sum(range(1, n + 1))
formula_a = n * (n + 1) / 2
print(f"Para n={n}:")
print(f"Soma real (lado esquerdo) = {soma_real_a}")
print(f"Valor da fórmula (lado direito) = {int(formula_a)}")
print(f"-> Válido? {soma_real_a == formula_a}")

# --- b. Soma de uma Progressão Geométrica ---
# Provar que 1+r+...+r^n = (1-r^(n+1))/(1-r)
print("\n--- b. Soma de uma Progressão Geométrica ---")
r_b = 3 # Usando um valor de exemplo para a razão r
soma_real_b = sum(r_b**i for i in range(n + 1))
formula_b = (1 - r_b**(n + 1)) / (1 - r_b)
print(f"Para n={n} e r={r_b}:")
print(f"Soma real (lado esquerdo) = {soma_real_b}")
print(f"Valor da fórmula (lado direito) = {int(formula_b)}")
print(f"-> Válido? {soma_real_b == formula_b}")

# --- c. Soma dos quadrados dos n primeiros inteiros ---
# Provar que 1²+2²+...+n² = n(n+1)(2n+1)/6
print("\n--- c. Soma dos quadrados dos n primeiros inteiros ---")
soma_real_c = sum(i**2 for i in range(1, n + 1))
formula_c = n * (n + 1) * (2*n + 1) / 6
print(f"Para n={n}:")
print(f"Soma real (lado esquerdo) = {soma_real_c}")
print(f"Valor da fórmula (lado direito) = {int(formula_c)}")
print(f"-> Válido? {soma_real_c == formula_c}")
