x = float(input())
valor = int(x * 100)

print(f"NOTAS:")

notas100 = valor // 10000
print(f"{notas100} nota(s) de R$ 100.00")
valor %= 10000

notas50 = valor // 5000
print(f"{notas50} nota(s) de R$ 50.00")
valor %= 5000

notas20 = valor // 2000
print(f"{notas20} nota(s) de R$ 20.00")
valor %= 2000

notas10 = valor // 1000
print(f"{notas10} nota(s) de R$ 10.00")
valor %= 1000

notas5 = valor // 500
print(f"{notas5} nota(s) de R$ 5.00")
valor %= 500

notas2 = valor // 200
print(f"{notas2} nota(s) de R$ 2.00")
valor %= 200

print("MOEDAS:")

moedas1 = valor // 100
print(f"{moedas1} moeda(s) de R$ 1.00")
valor %=  100

moedas50 = valor // 50
print(f"{moedas50} moeda(s) de R$ 0.50")
valor %= 50

moedas25 = valor // 25
print(f"{moedas25} moeda(s) de R$ 0.25")
valor %= 25

moedas10 = valor // 10
print(f"{moedas10} moeda(s) de R$ 0.10")
valor %= 10

moedas5 = valor // 5
print(f"{moedas5} moeda(s) de R$ 0.05")
valor %= 5

moedas01 = valor // 1
print(f"{moedas01} moeda(s) de R$ 0.01")



