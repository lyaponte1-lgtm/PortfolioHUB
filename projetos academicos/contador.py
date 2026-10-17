quantidade = 0 
aprovados = 0
reprovados = 0
soma = 0 
while True:
    nota = float(input("Digite a nota do aluno (ou -1 para sair): "))
    
    if nota == -1:
        break
    
    quantidade += 1
    soma += nota
    
    if nota >= 7:
        aprovados += 1
    else:
        reprovados += 1
if quantidade > 0:
    media = soma / quantidade
else : 
    media = 0

print(f"Quantidade de alunos: {quantidade}")
print(f"Quantidade de alunos aprovados: {aprovados}")
print(f"Quantidade de alunos reprovados: {reprovados}")
print(f"Média das notas: {media}")
