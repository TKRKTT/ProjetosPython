# caixa_eletronico_app.py - Aplicação principal do simulador de caixa eletrônico

# Importa as funções de operações bancárias do módulo operacoes_bancarias.
from operacoes_bancarias import consultar_saldo, depositar, sacar

def exibir_menu():
    """
    Exibe as opções do menu do caixa eletrônico.
    """
    print("\n----- MENU DO CAIXA ELETRÔNICO -----")
    print("1 - Consultar Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    print("------------------------------------")

def main():
    """
    Função principal que gerencia o fluxo do programa.
    """
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            saldo_atual = consultar_saldo()
            print(f"\n--- SALDO ATUAL ---")
            print(f"Saldo disponível: R$ {saldo_atual:.2f}")
            print(f"-------------------\n")

        elif opcao == "2":
            try:
                valor_deposito = float(input("Digite o valor a ser depositado: R$ "))
                if depositar(valor_deposito):
                    print(f"\nDepósito de R$ {valor_deposito:.2f} realizado com sucesso!")
                else:
                    print("\nValor de depósito inválido. Por favor, digite um valor positivo.")
            except ValueError:
                print("\nEntrada inválida. Por favor, digite um número para o valor.")
                
        elif opcao == "3":
            try:
                valor_saque = float(input("Digite o valor a ser sacado: R$ "))
                resultado_saque = sacar(valor_saque)
                if resultado_saque:
                    print(f"\nSaque de R$ {valor_saque:.2f} realizado com sucesso!")
                else:
                    # Verifica a razão da falha no saque
                    if valor_saque <= 0:
                        print("\nValor de saque inválido. Por favor, digite um valor positivo.")
                    else: # Se não for valor inválido, é saldo insuficiente
                        print("\nSaldo insuficiente. Não é possível realizar o saque.")
                # Sempre mostra o saldo atual após uma tentativa de saque/depósito
                saldo_atual = consultar_saldo()
                print(f"Saldo disponível: R$ {saldo_atual:.2f}")
            except ValueError:
                print("\nEntrada inválida. Por favor, digite um número para o valor.")

        elif opcao == "4":
            print("\nSaindo do sistema... Obrigado por usar nosso caixa eletrônico!")
            break
        else:
            print("\nOpção inválida. Por favor, escolha uma opção entre 1 e 4.")

# Garante que a função main() seja executada apenas quando o script é rodado diretamente
if __name__ == "__main__":
    main()

