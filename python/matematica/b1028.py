import math

x = int(input())

for i in range(x):
    a , b = map(int, input().split())
    c =math.gcd(a,b)
    print(c)
