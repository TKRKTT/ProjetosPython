# exercio03.py - Lista de frutas em python

frutas = ["maçã", "banana", "laranja", "melão", "abacaxi"]

print("Lista de frutas favoritas são:", frutas)

primeira_fruta = frutas[0]
segunda_fruta = frutas[1]

print(f"A primeira fruta é: {primeira_fruta}, e a segunda fruta é: {segunda_fruta}")

frutas.append("uva")
print("Lista de frutas atualizada:", frutas)

frutas.remove("banana")
print("Lista de frutas após remoção da banana:", frutas)

quantidade_frutas = len(frutas)
print(f"Quantidade de frutas na lista: {quantidade_frutas}")

print("\n --- Percorendo as frutas na lista ---")
for fruta in frutas:
    print(f"Frutas: {frutas}")
    print("fim exercício03.py")
    
    break
# Exercício 03 - Python Básico com Listas