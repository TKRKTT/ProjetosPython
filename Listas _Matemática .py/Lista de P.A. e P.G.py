# -*- coding: utf-8 -*-

# =============================================================================
# SOLUÇÃO COMPLETA: LISTA DE P.A. E P.G. (VERSÃO CORRIGIDA)
# Este script adapta TODAS as questões da lista para código Python.
# =============================================================================

def imprimir_titulo(titulo):
    """Função auxiliar para imprimir títulos formatados."""
    print("\n\n" + "="*60)
    print(f"--- {titulo} ---")
    print("="*60)

# --- Funções Genéricas ---
def pa_termo_geral(a1, r, n):
    return a1 + (n - 1) * r

def pa_soma(a1, an, n):
    return (a1 + an) * n / 2

def pa_encontrar_n(a1, an, r):
    return int(((an - a1) / r) + 1)

def pg_termo_geral(a1, q, n):
    return a1 * (q ** (n - 1))

def pg_soma_finita(a1, q, n):
    if q == 1:
        return a1 * n
    return a1 * (q**n - 1) / (q - 1)

def pg_soma_infinita(a1, q):
    if abs(q) < 1:
        return a1 / (1 - q)
    return "Não converge"

# =============================================================================
# INÍCIO DAS SOLUÇÕES
# =============================================================================

imprimir_titulo("Questão 1: Encontrar o 14º termo da P.A.")
print(f"a. A=(4,10,...): a14 = {pa_termo_geral(a1=4, r=6, n=14)}")
print(f"c. C=(8,2,...): a14 = {pa_termo_geral(a1=8, r=-6, n=14)}")
print(f"d. D=(3,10,17,...): a14 = {pa_termo_geral(a1=3, r=7, n=14)}")

imprimir_titulo("Questão 2: Calcular a soma dos termos da P.A.")
n_a = pa_encontrar_n(a1=4, an=604, r=8)
print(f"a. A=(4,12,...,604): Soma = {pa_soma(a1=4, an=604, n=n_a)}")
n_c = pa_encontrar_n(a1=8, an=-192, r=-10)
print(f"c. C=(8,-2,...,-192): Soma = {pa_soma(a1=8, an=-192, n=n_c)}")
n_d = pa_encontrar_n(a1=3, an=206, r=7)
print(f"d. D=(3,10,17,...,206): Soma = {pa_soma(a1=3, an=206, n=n_d)}")

imprimir_titulo("Questão 3: Encontrar o 12º termo da P.G.")
print(f"a. A=(4,8,16,...): a12 = {pg_termo_geral(a1=4, q=2, n=12)}")
print(f"b. B=(5, 5/3,...): a12 = {pg_termo_geral(a1=5, q=1/3, n=12):.10f}")
print(f"c. C=(8,2,1/2,...): a12 = {pg_termo_geral(a1=8, q=1/4, n=12):.10f}")
print(f"d. D=(3,15,75,...): a12 = {pg_termo_geral(a1=3, q=5, n=12)}")

imprimir_titulo("Questão 4: Calcular a soma dos 12 primeiros termos da P.G.")
print(f"a. A=(4,8,16,...): S12 = {pg_soma_finita(a1=4, q=2, n=12)}")
print(f"b. B=(5,15,45,...): S12 = {pg_soma_finita(a1=5, q=3, n=12)}")
print(f"c. C=(7,14,28,...): S12 = {pg_soma_finita(a1=7, q=2, n=12)}")
print(f"d. D=(3,15,75,...): S12 = {pg_soma_finita(a1=3, q=5, n=12)}")

imprimir_titulo("Questão 5: Calcular a soma dos infinitos termos da P.G.")
print(f"a. A=(5, 5/3,...): S_inf = {pg_soma_infinita(a1=5, q=1/3)}")
print(f"b. B=(8, 2, 1/2,...): S_inf = {pg_soma_infinita(a1=8, q=1/4)}")

imprimir_titulo("Questão 6: Sequência de ímpares")
# A quantidade de elementos na linha n é n.
# O último elemento da linha n-1 é a soma das quantidades das linhas anteriores.
# Último número da linha 30 = 2 * (soma dos números de 1 a 30) - 1
soma_ate_30 = sum(range(1, 31))
ultimo_numero_linha_30 = 2 * soma_ate_30 - 1
primeiro_elemento_linha_31 = ultimo_numero_linha_30 + 2
print(f"a. O primeiro elemento da 31ª linha é: {primeiro_elemento_linha_31}")

# A soma dos elementos da linha n é n³.
soma_elementos_linha_31 = 31**3
print(f"b. A soma dos elementos da 31ª linha é: {soma_elementos_linha_31}")

imprimir_titulo("Questão 7: Distância percorrida pela bola")
h0 = 5
razao = 4/9
# A distância é a queda inicial + 2 * (soma das alturas que sobe)
# As subidas formam uma PG infinita com a1 = 5*(4/9)
dist_subidas = pg_soma_infinita(a1=h0 * razao, q=razao)
dist_total = h0 + 2 * dist_subidas
print(f"A distância total percorrida pela bola é: {dist_total:.2f} cm")

imprimir_titulo("Questão 8: Sequência de somas")
# O primeiro termo da linha n é o (n(n-1)/2 + 1)-ésimo ímpar? Não, é o número natural.
# Primeiro número da linha n: (n*(n-1)/2) + 1
def primeiro_termo_linha(n):
    return (n * (n - 1) // 2) + 1

# a. Menor e maior inteiro de a10
linha = 10
menor_inteiro = primeiro_termo_linha(linha)
maior_inteiro = menor_inteiro + linha - 1
print(f"a. Para a10, o menor inteiro é {menor_inteiro} e o maior é {maior_inteiro}")

# b. Calcule a10
# É a soma de uma P.A. com a1=menor, an=maior, n=10
soma_a10 = pa_soma(a1=menor_inteiro, an=maior_inteiro, n=linha)
print(f"b. O valor de a10 é: {int(soma_a10)}")

# c. Expressão geral para an
# an é a soma dos n termos da P.A. que começa em (n(n-1)/2 + 1)
# an = (primeiro + ultimo) * n / 2
# an = ( (n(n-1)/2 + 1) + (n(n-1)/2 + n) ) * n / 2
# an = ( n(n-1) + n + 1 ) * n / 2
# an = (n² - n + n + 1) * n / 2 = (n² + 1) * n / 2
n_teste = 10
formula_an = (n_teste**2 + 1) * n_teste / 2
print(f"c. A expressão geral para an é (n² + 1)*n / 2.")
print(f"   Verificando para n=10: {int(formula_an)} (confere com o item b)")

