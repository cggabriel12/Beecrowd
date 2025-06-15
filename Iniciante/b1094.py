N = int(input())
total = 0
coelho = 0
sapo = 0
rato = 0

for i in range(N):
    quantidade , animal = input().split()
    quantidade = int(quantidade)
    total += quantidade
    if animal == "C":
        coelho += quantidade
    elif animal == "R":
        rato += quantidade
    elif animal == "S":
        sapo += quantidade

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}")
print(f"Total de sapos: {sapo}")

print(f"Percentual de coelhos: {coelho / total * 100:.2f} %")
print(f"Percentual de ratos: {rato / total * 100:.2f} %")
print(f"Percentual de sapos: {sapo / total * 100:.2f} %")
