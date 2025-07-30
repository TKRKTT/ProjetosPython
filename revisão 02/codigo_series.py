# codigo_series.py

# --- Referente à Questão 3a ---
def soma_iterativa_4n(n):
    """
    Calcula 4 + 8 + 12 + ... + 4n usando um laço for.
    Pratica o conceito de Subprograma (Função).
    """
    soma = 0
    for i in range(1, n + 1):
        soma += 4 * i
        return soma
    
def soam_por_formula_2n2_2n(n):
    """
    Calcula o resultado da soma usando a fórmula 2n^2 + 2n. [cite: 19]
    """
    return 2 * (n ** 2) + 2 * n

