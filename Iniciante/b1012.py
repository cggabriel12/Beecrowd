a , b , c = input().split()
a = float(a)
b = float(b)
c = float(c)
pi = 3.14159

tri = a * c / 2
circ = pi * c**2
trap = (a + b) * c / 2
quad = b**2
reta = a * b

print(f"TRIANGULO: {tri:.3f}")
print(f"CIRCULO: {circ:.3f}")
print(f"TRAPEZIO: {trap:.3f}")
print(f"QUADRADO: {quad:.3f}")
print(f"RETANGULO: {reta:.3f}")
