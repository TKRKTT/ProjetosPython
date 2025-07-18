# exercicio03.py - Lista de frutas em python # 'exercio' corrigido

frutas = ["maçã", "banana", "laranja", "melão", "abacaxi"]

print("\n Lista de frutas favoritas são:", frutas)

primeira_fruta = frutas[0]
segunda_fruta = frutas[1]

print(f"A primeira fruta é: {primeira_fruta}, e a segunda fruta é: {segunda_fruta}")

frutas.append("uva")
print("\nLista de frutas atualizada:", frutas)

frutas.remove("banana")
print("\nLista de frutas após remoção da banana:", frutas)

quantidade_frutas = len(frutas)
print(f"\n Quantidade de frutas na lista: {quantidade_frutas}")

frutas.insert(2, "Kiwi")
print("\nLista de frutas após inserção do Kiwi:", frutas)

del frutas[3]
print("Lista de frutas após remoção do elemnto do indice 3:", frutas)

if "morango" in frutas:
    print("\n --- Morango está na lista de frutas ---")
else:
    print("\n --- Morango não está na lista de frutas ---")

print("\n --- Percorrendo as frutas na lista ---") # 'Percorendo' corrigido
for fruta in frutas:
    print(f"- {frutas}") # Lembre-se, aqui você provavelmente queria printar '- {fruta}' e não '{frutas}'

print("----- fim do exercício03.py -----")
# Exercício 03 - Python Básico com Listas