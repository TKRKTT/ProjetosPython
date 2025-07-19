# Questão03.py - Dicionário de notas de um aluno

notas_aluno = {
    "Matemática": 8.5,
    "Português": 7.0, # 'Portuguẽs' corrigido para 'Português' (e removido o til para boa prática)
    "História": 9.0,
    "Ciências": 6.5 # 'Ciẽncias' corrigido para 'Ciências' (e removido o til para boa prática)
}

# A linha 'disciplina = notas_aluno' foi removida, pois não é utilizada e pode causar confusão.

print(" --- Notas do Aluno ---")
print(f"Dicionário completo: {notas_aluno}")

notas_aluno["Inglês"] = 7.5 # 'Inglẽs' corrigido para 'Inglês' (e removido o til para boa prática)
print(f"\nNova nota adicionada: Inglês - {notas_aluno['Inglês']}")

notas_aluno["Matemática"] = 9.5
print(f"\n Nota de Matemática alterada: {notas_aluno['Matemática']}")

print("\n --- Percorrendo as Disciplinas e Notas ---")
for disciplina, nota_atual in notas_aluno.items(): # 'intems()' corrigido para 'items()'
    print(f"Disciplina: {disciplina}, nota: {nota_atual}") # Variável 'nota_atual' usada corretamente

print("\n --- fim do exercício ---")
