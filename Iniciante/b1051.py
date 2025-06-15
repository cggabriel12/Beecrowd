num1 = float(input())

if  num1 <= 2000:
    print("Isento")
elif num1 <= 3000:
    imposto = (num1 - 2000) * 0.08
    print(f"R$ {imposto:.2f}")
elif num1 <= 4500:
    imposto = (3000 - 2000) * 0.08
    impost2 = (num1 - 3000) * 0.18
    print(f"R$ {imposto + impost2:.2f}")
else:
    imposto = (3000 - 2000) * 0.08
    impost2 = (4500 - 3000) * 0.18
    impost3 = (num1 - 4500) * 0.28
    print(f"R$ {imposto + impost2 + impost3:.2f}")
