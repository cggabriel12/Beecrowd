num = []
numeros = 0

for i in range(12):
    num.append([0] * 12)

numero = int(input())
operacao = input()
for i in range(12):
    for j in range(12):
        num[i][j] = float(input())

if operacao == "S":
    for j in range(12):
        numeros += num[numero][j]
    print(numeros)
elif operacao == "M":
    for j in range(12):
        numeros +=  num[numero][j]
    print(f"{numeros/len(num):.1f}")
