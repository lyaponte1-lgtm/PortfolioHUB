soma_pares = 0
quantidade_pares = 0

soma_impares = 0
quantidade_impares = 0

while True:
    numero = int(input("Digite um número (ou -1 para sair): "))
    
    if numero == -1:
        break
    
    if numero % 2 == 0:
        soma_pares += numero
        quantidade_pares += 1
    else:
        soma_impares += numero
        quantidade_impares += 1
if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
else:
    media_pares = 0

if quantidade_impares > 0:
    media_impares = soma_impares / quantidade_impares
else:
    media_impares = 0
