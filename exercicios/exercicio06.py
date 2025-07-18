# exercicio06.py - Gerenciador de tarefas simples

# Lista global para armazenar as tarefas (cada tarefa será um dicionário)
tarefas = []

# --- Funções para gerenciar as tarefas ---

def adicionar_tarefa(nome_tarefa):
    global tarefas # Declara que vamos usar a variável global 'tarefas'
    nova_tarefa = {"nome": nome_tarefa, "concluida": False} # Cria o dicionário da tarefa
    tarefas.append(nova_tarefa) # Adiciona o dicionário à lista global
    print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")

def listar_tarefas():

    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("Lista de Tarefas:")
        # O 'enumerate' por padrão começa do 0. Usamos 'start=1' para numerar para o usuário
        for i, tarefa_atual in enumerate(tarefas, start=1):
            status = "Concluída" if tarefa_atual["concluida"] else "Pendente"
            print(f"{i}. {tarefa_atual['nome']} - {status}")

def marcar_tarefa_concluida(indice):
    global tarefas # Declara que vamos usar a variável global 'tarefas'
    # Ajusta o índice fornecido pelo usuário (que começa em 1) para o índice real da lista (que começa em 0)
    indice_real = indice - 1

    if 0 <= indice_real < len(tarefas):
        tarefas[indice_real]['concluida'] = True
        print(f"Tarefa '{tarefas[indice_real]['nome']}' marcada como concluída.")
    else:
        # Imprime o índice original digitado pelo usuário na mensagem de erro
        print(f"Erro: Índice {indice} inválido. Não há tarefa com esse índice.")

# --- Função Principal do Programa (Menu) ---
def main():
    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite o nome da tarefa: ")
            adicionar_tarefa(nome)
        elif escolha == '2':
            listar_tarefas()
        elif escolha == '3':
            try:
                indice = int(input("Digite o NÚMERO (ex: 1 para a primeira) da tarefa a ser marcada como concluída: "))
                marcar_tarefa_concluida(indice)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro válido para o índice.")
        elif escolha == '4': # Opção para sair
            print("Saindo do Gerenciador de Tarefas. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida (1, 2, 3 ou 4).")

# --- Execução do programa ---
if __name__ == "__main__":
    main()