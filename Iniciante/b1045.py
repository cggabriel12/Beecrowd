lados  = list(map(float , input().split()))

lados.sort(reverse = True)
a , b , c = lados

if a >= b + c:
  print("NAO FORMA TRIANGULO")
else:
  if a **2 == b **2 + c **2:
    print("TRIANGULO RETANGULO")
  if a ** 2> b**2 + c**2:
    print("TRIANGULO OBTUSANGULO")
  if a**2 < b**2 + c**2:
    print("TRIANGULO ACUTANGULO")
  if a == b and a == c:
    print("TRIANGULO EQUILATERO")
  elif(a==b and b!=c) or (b==c and c!=a) or (c==a and b!=a):
    print("TRIANGULO ISOSCELES")