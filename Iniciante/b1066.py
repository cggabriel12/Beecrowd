soma = 0
impar = 0
positivo = 0
negativo = 0
for i in range(5):
    num1 = int(input())
    if num1 % 2 == 0:
        soma += 1
    elif num1 % 2 != 0:
        impar += 1
    if num1 > 0:
        positivo += 1
    elif num1 < 0:
        negativo += 1

print(f"{soma} valor(es) par(es)")
print(f"{impar} valor(es) impar(es)")
print(f"{positivo} valor(es) positivo(s)")
print(f"{negativo} valor(es) negativo(s)")
          

