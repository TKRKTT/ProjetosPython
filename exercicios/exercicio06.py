# exercicio06.py - Gerenciador de tarefas simples # 'Gerinciandor' corrigido

# Lista global para armazenar as tarefas (cada tarefa será um dicionário) # 'Liata' e 'taefa' corrigidos
tarefas = []

# --- Funções para gerenciar as tarefas ---

def adicionar_tarefa(nome_tarefa):
    global tarefas # Declara que vamos usar a variável global 'tarefas'
    nova_tarefa = {"nome": nome_tarefa, "concluida": False} # Cria o dicionário da tarefa
    tarefas.append(nova_tarefa) # Adiciona o dicionário à lista global
    print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")

def listar_tarefas():
    # global tarefas # Não é estritamente necessário aqui, pois a função apenas lê a lista global
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print("Lista de Tarefas:")
        # O 'enumerate' por padrão começa do 0. Usamos 'start=1' para numerar para o usuário
        for i, tarefa_atual in enumerate(tarefas, start=1): # 'tarefas' no loop corrigido para 'tarefa_atual', 'strart' para 'start'
            status = "Concluída" if tarefa_atual["concluida"] else "Pendente" # Adicionado para mostrar o status
            print(f"{i}. {tarefa_atual['nome']} - {status}")

def marcar_tarefa_concluida(indice):
    global tarefas # Declara que vamos usar a variável global 'tarefas'
    # Ajusta o índice fornecido pelo usuário (que começa em 1) para o índice real da lista (que começa em 0)
    indice_real = indice - 1

    if 0 <= indice_real < len(tarefas):
        tarefas[indice_real]['concluida'] = True
        print(f"Tarefa '{tarefas[indice_real]['nome']}' marcada como concluída.") # 'com' corrigido para 'como'
    else:
        # Imprime o índice original digitado pelo usuário na mensagem de erro
        print(f"Erro: Índice {indice} inválido. Não há tarefa com esse índice.") # 'indice' corrigido para 'índice'

# --- Função Principal do Programa (Menu) ---
def main():
    while True:
        print("\n--- Gerenciador de Tarefas ---") # 'Gerenciadoor' corrigido
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída") # 'concluida' corrigido
        print("4. Sair") # Adicionada opção 4. Sair no menu

        escolha = input("Escolha uma opção: ") # 'um' corrigido para 'uma'

        if escolha == '1':
            nome = input("Digite o nome da tarefa: ")
            adicionar_tarefa(nome)
        elif escolha == '2':
            listar_tarefas()
        elif escolha == '3':
            try:
                indice = int(input("Digite o NÚMERO (ex: 1 para a primeira) da tarefa a ser marcada como concluída: ")) # 'índice' corrigido
                marcar_tarefa_concluida(indice)
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro válido para o índice.") # 'inteiro' adicionado, 'índice' corrigido
        elif escolha == '4': # Opção para sair
            print("Saindo do Gerenciador de Tarefas. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida (1, 2, 3 ou 4).") # 'invalida' e 'valida' corrigidos

# --- Execução do programa ---
if __name__ == "__main__":
    main()
