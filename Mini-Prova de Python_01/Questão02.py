# Questão02.py - Manipulação de Lista de Produtos

produtos = ["Monitor", "Teclado", "Mouse", "Webcam", "Fone de Ouvido"]

if "Mouse" in produtos:
    print(" --- Mouse encontrado! ---")
else:
    produtos.append("Mouse")
    print("Mouse não estava na lista e agora foi adicionado.")
    print("O Mouse não está na lista de produtos.") # Esta linha pode ser redundante se o mouse for adicionado.
    print("Lista de produtos atualizada:", produtos)

print("\n Lista de produtos:", produtos)

del produtos[1] # Removendo o Teclado
print("\n Lista de produtos após remoção do Teclado:", produtos)

print(" --- Fim do exercício ---")
