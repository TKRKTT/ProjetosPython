# operacoes_bancarias.py - Módulo para as funções de operações bancárias

# Define o saldo inicial do banco.
# Esta variável será acessada e modificada pelas funções neste módulo.
_saldo = 10000.0  # Usamos um underscore para indicar que é uma variável "interna" ao módulo

def consultar_saldo():
    """
    Retorna o saldo atual da conta
    """
    return _saldo

def depositar(valor):
    """
    Realiza um depósito na conta.
    Retorna True se o depósito for bem-sucedido, False caso contrário.
    """
    global _saldo # Declara que vamos modificar a variável global '_saldo'
    if valor > 0:
        _saldo += valor
        return True
    else:
        return False
    
def sacar(valor):
    """
    Realiza um saque da conta.
    Retorna True se o saque for bem-sucedido, False caso contrário.
    """
    global _saldo # Declara que vamos modificar a variável global '_saldo'
    if valor <= 0:
        return False # Valor inválido para saque
    elif valor > _saldo:
        return False # Saldo insuficiente
    else:
        _saldo -= valor
        return True
