ini = 7
fim = 4

for i in range(1 , 10 , 2):
    for j in range(ini, fim , -1):
        print(f"I={i} J={j}")
    ini += 2
    fim += 2