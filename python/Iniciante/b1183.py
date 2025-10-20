num = []
numeros = 0

for i in range(12):
    num.append([0] * 12)

operacao = input()

for i in range(12):
    for j in range(12):
        num[i][j] = float(input())

for i in range(12):
    for j in range(12):
        if j > i:
            numeros += num[i][j]
if operacao == "S":
    print(numeros)
elif operacao == "M":
    print(f"{numeros / (len(num) * (12 - 1)/2):.1f}")
