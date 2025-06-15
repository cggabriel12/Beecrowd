x = int(input()) 
qtd = 1

while True:
    if x % 2 != 0:
        print(x) 
        qtd += 1
    if qtd == 7:
        break
    x += 1
