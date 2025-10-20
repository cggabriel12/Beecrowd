N = int(input())

for i in range(N):
    x , y = map(int , input().split())
    impares = 0
    if x > y:
        maior = x
    else:
        maior = y
    if x < y:
        menor = x
    else:
        menor = y
    for j in range(menor + 1 , maior):
        if j % 2 !=0:
            impares += j
    print(impares)
        