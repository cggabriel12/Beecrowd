import math

while True:
    try:
        x, y, z = map(int, input().split())

        
        lados = sorted([x, y, z])
        x, y, z = lados

        
        if x**2 + y**2 == z**2:
            
            mdc = math.gcd(x, math.gcd(y, z))
            if mdc == 1:
                print("tripla pitagorica primitiva")
            else:
                print("tripla pitagorica")
        else:
            print("tripla")

    except EOFError:
        break
