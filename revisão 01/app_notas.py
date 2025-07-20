# app_notas.py - Aplicação principal do Sistema de Gerenciamento de Notas

# Importa as funções do módulo gerenciador_notas
from gerenciador_notas import (
    adicionar_aluno,
    adicionar_nota_a_aluno,
    listar_alunos_e_medias,
    alunos # Importando a lista para a verificação de saída
)

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    # CORREÇÃO: Erro de digitação
    print("\n--- Sistema de Gerenciamento de Notas ---")
    print("1. Adicionar Aluno")
    print("2. Adicionar Nota")
    print("3. Listar Alunos e Médias")
    print("4. Sair")
    print("-----------------------------------------")

# CORREÇÃO DE ESTRUTURA: A função 'main' foi movida para fora da 'exibir_menu'
def main():
    """Função principal que executa a aplicação."""
    # CORREÇÃO DE SINTAXE: Trocado ';' por ':'
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            # --- Lógica para adicionar aluno ---
            nome_aluno = input("Digite o nome do novo aluno: ")
            adicionar_aluno(nome_aluno)

        elif opcao == '2':
            # --- Lógica para adicionar nota ---
            if not alunos:
                # CORREÇÃO: Erro de digitação
                print("É preciso cadastrar um aluno primeiro.")
                continue # Volta para o início do loop

            nome_aluno = input("Digite o nome do aluno: ")
            try:
                nota = float(input("Digite a nota (de 0 a 10): "))
                if 0 <= nota <= 10:
                    adicionar_nota_a_aluno(nome_aluno, nota)
                else:
                    print("Erro: A nota deve ser um valor entre 0 e 10.")
            except ValueError:
                # CORREÇÃO: Erro de digitação
                print("Erro: Por favor, insira um valor numérico para a nota.")

        elif opcao == '3':
            # --- Lógica para listar alunos ---
            # CORREÇÃO DE LÓGICA: Adicionado '()' para executar a função
            listar_alunos_e_medias()

        elif opcao == '4':
            # --- Lógica para sair ---
            # CORREÇÃO: Erro de digitação
            print("Saindo do sistema. Até logo!")
            break # Encerra o loop while

        else:
            # CORREÇÃO: Erro de digitação
            print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")

# Garante que o programa principal só será executado quando este arquivo for rodado diretamente
if __name__ == "__main__":
    main()