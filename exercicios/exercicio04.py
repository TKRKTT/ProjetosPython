# exercicio04.py - Dicionário em Python # 'Dicinário' corrigido

# 1. Criando um dicionário de uma pessoa
# Cada item é par chave: valor # 'intem' corrigido
pessoa = {
    "nome": "Osvado",
    "idade": 30,
    "cidade": "Arapiraca",
    "profissao": "Programador"
}

print("--- Informações da pessoa ---") # 'passoa' corrigido
print(f"Dicionário completo: {pessoa}")

# 2. Acessando valores usando as chaves
nome_pessoa = pessoa["nome"] # 'nome_pssoa' corrigido para 'nome_pessoa'
idade_pessoa = pessoa["idade"]
print(f"\nNome: {nome_pessoa}")
print(f"Idade: {idade_pessoa} anos")

# 3. Alterando valores
pessoa["idade"] = 545
print(f"\nIdade alterada: {pessoa['idade']} anos")

# 4. Adicionando um novo par chave-valor
pessoa["email"] = "Osvado@freefireMAX.com"
print(f"\n Novo email adicionado: {pessoa['email']}")

# 5. Removendo um par chave-valor
del  pessoa["profissao"]
print("\nProfissão removida do dicionário:", pessoa)

# 6. Verificando se uma chave existe no dicionário
if "cidade" in pessoa:
    print("\nCidade da pessoa:", pessoa['cidade'])
else:
    print("\nCidade não encontrada no dicionário.") # 'encoontrada' e 'dicinário' corrigidos

if "telefone" in pessoa:
    print("\n Telefone da pessoa:", pessoa['telefone'])
else:
    print("\n Telefone não encontrado no dicionário.")

# 7. Percorrendo o dicionário(Iterando)
print("\n --- Percorrendo o dicionário (chaves) ---")
for chave in pessoa:
    print(f" Chave: {chave}")

print("\n --- Percorrendo o dicionário (valores)")
for valor in pessoa.values():
    print(f"valor: {valor}")

print("\n --- Percorrendo o dicionário (chave-valor) ---")
for chave, valor in pessoa.items():
    print(f"Chave: {chave}, Valor: {valor}")

print("\n ----- fim do exercício04.py -----")