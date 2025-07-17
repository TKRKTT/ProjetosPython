# exercicio04.py - Dicinário em Python

# 1. Criando um dicionário de uma pessoa
# Cada intem é par chave: valor
pessoa = {
    "nome": "Osvado",
    "idade": 30,
    "cidade": "Arapiraca",
    "profissao": "Programador"
}

print("--- Informações da passoa ---")
print(f"Dicionário completo: {pessoa}")

# 2. Acessando valores usando as chaves
nome_pssoa = pessoa["nome"]
idade_pessoa = pessoa["idade"]
print(f"\nNome: {nome_pssoa}")
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
    print("\nCidade não encoontrada no dicinário.")

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