num1 , num2 , num3 = input().split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

segundo_maior = (num1 + num2 + abs (num1 - num2))/2
maior = (segundo_maior + num3 + abs (segundo_maior - num3))/2
print(f"{int(maior)} eh o maior")
