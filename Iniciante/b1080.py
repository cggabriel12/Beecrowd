num = []

for i in range(100):
    num.append(int(input()))



maior = max(num)
indice = num.index(max(num))

print(maior)
print(indice + 1)
