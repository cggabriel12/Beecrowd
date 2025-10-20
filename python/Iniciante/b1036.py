num1 , num2 , num3 = input().split()
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)
delta = num2**2 -4 * num1 * num3

if num1 != 0 and delta >= 0:
    bhaskara_positiva = (-num2 + delta**0.5) / (2 * num1)
    bhaskara_negativa = (-num2 - delta**0.5) / (2 * num1)
    print(f"R1 = {bhaskara_positiva:.5f}")
    print(f"R1 = {bhaskara_negativa:.5f}")
else:
    print("Impossivel calcular")