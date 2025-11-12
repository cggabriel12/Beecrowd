import math

while True:
    try:
        n = int(input())
        qtd = 0  

        if n > 1:
            
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    qtd += 1
                    break 

            if qtd > 0:
                print("Nada")
            else:
                
                t = str(n)
                qtdt = 0
                for i in t:
                    if int(i) in [2, 3, 5, 7]:
                        qtdt += 1
                if qtdt == len(t):
                    print("Super")
                else:
                    print("Primo")
        else:
            print("Nada")

    except EOFError:
        break
