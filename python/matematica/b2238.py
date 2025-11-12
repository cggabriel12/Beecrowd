import math

A, B, C, D = map(int, input().split())

ca = []


i = 1
while i * i <= C:
    if C % i == 0:
        ca.append(i)
        if i * i != C:
            ca.append(C // i)
    i += 1

ca.sort()

re = -1
for n in ca:
    if n % A != 0:      
        continue
    if n % B == 0:      
        continue
    if D % n == 0:      
        continue
    re = n
    break

print(re)
