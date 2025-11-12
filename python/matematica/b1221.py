x = int(input())

for i in range(x):
    n = int(input())
    qtd = 0
    if n > 1:
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                qtd +=1
        

        if qtd > 0:
            print("Not Prime")
        else:
            print("Prime")
