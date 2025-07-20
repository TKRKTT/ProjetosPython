# gerenciador_notas.py - Módulo para a lógica de gerenciamento de notas

# Lista global para armazenar os dicionários de alunos
alunos = []

# --- Funções Auxiliares ---

def calcular_media(lista_de_numeros):
    """
    Calcula a média de uma lista de números.
    Recebe: uma lista de números (list).
    Retorna: a média dos números (float).
    """
    if not lista_de_numeros:
        return 0.0
    soma = sum(lista_de_numeros)
    quantidade = len(lista_de_numeros)
    return soma / quantidade

# --- Funções do Sistema de Notas ---

def adicionar_aluno(nome):
    """
    Adiciona um novo aluno à lista global de alunos.
    Recebe o nome do aluno.
    """
    if not nome:
        print("Nome do aluno não pode ser vazio.")
        return False
    
    # Verifica se o aluno já existe
    for aluno_existente in alunos:
        if aluno_existente["nome"].lower() == nome.lower():
            print(f"Aluno '{nome}' já cadastrado.")
            return False
        
    novo_aluno = {"nome": nome, "notas":[]}
    alunos.append(novo_aluno)
    print(f"Aluno '{nome}' adicionado com sucesso!")
    return True

def adicionar_nota_a_aluno(nome_aluno, nota):
    """
    Adiciona uma nota a um aluno existente.
    Recebe o nome do aluno e a nota.
    """
    aluno_encontrado = None
    for aluno in alunos:
        if aluno["nome"].lower() == nome_aluno.lower(): # Corrigido 'lawer()' para 'lower()'
            aluno_encontrado = aluno
            break

    if aluno_encontrado:
       # A validação da nota (0 a 10 e tipo numérico) será feita na interface (app_notas.py)
       aluno_encontrado["notas"].append(nota) # Corrigido: adiciona à lista 'notas', não ao 'nome'
       print(f"Nota {nota:.1f} adicionada para o aluno: {aluno_encontrado['nome']}") # Corrigido 'adicionado' para 'adicionada'
       return True
    else:
        print(f"Aluno '{nome_aluno}' não encontrado.")
        return False

def listar_alunos_e_medias(): # Corrigido nome da função: 'e_madia' para 'e_medias'
    """
    Lista todos os alunos, suas notas, calcula e exibe a média e o status (Aprovado/Reprovado).
    """
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    print("\n--- Lista de Alunos e Médias ---") # Corrigido 'Lista da Alunos' para 'Lista de Alunos'
    for aluno in alunos:
        print(f"\nAluno: {aluno['nome']}")
        if aluno["notas"]: # Adicionado 'if' para verificar se há notas antes de calcular a média
            media = calcular_media(aluno['notas']) # Corrigido: passando 'aluno['notas']', não 'aluno['nome']'
            print(f"  Notas: {aluno['notas']}")
            print(f"  Média: {media:.2f}")
            if media >= 7.0:
                print("  Status: Aprovado")
            else:
                print("  Status: Reprovado")
        else: # Este 'else' agora está corretamente aninhado ao 'if aluno["notas"]:'
            print("  Sem notas cadastradas.")