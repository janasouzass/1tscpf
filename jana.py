tit = "Menor, Intermediário e Maior"

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

print(f'Os números {n1}, {n2}, {n3},',end= ' ')

if n1 > 2:
    n1, n2 = n2, n1

if n1 > n3:
    n1, n3 = n3, n1

if n2 > n3:
    n2, n3 = n3, n2

print(f'São menor: {n1}, itermediario: {n2}, maior: {n3}')
