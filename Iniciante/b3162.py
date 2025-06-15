naves = int(input())

for i in range(naves):
    
    distancia1 , distancia2 , distancia3 = map(int, input().split())
    
    maior = max(distancia1 , distancia2 , distancia3)
    
    if maior == distancia1:
        print("A")
    elif maior == distancia2:
        print("M")
    elif maior == distancia3:
        print("B")