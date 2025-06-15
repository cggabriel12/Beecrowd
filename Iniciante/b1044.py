num1 , num2 = input().split()
num1 = int(num1)
num2 = int(num2)

maior = (num1 + num2 + abs (num1 - num2))/2
menor = (num1 + num2 - abs(num1 - num2)) / 2
if maior % menor == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")