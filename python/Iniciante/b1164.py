t = int(input().strip())

for i in range(t):
    n = int(input().strip())
    if n == 1:
        print(f"{n} nao eh perfeito")
        continue

    s = 0
    l = int(n**0.5)
    for j in range(1, l + 1):
        if n % j == 0:
            d1 = j
            d2 = n // j
            if d1 != n:
                s += d1
            if d2 != d1 and d2 != n:
                s += d2
    if s == n:
        print(f"{n} eh perfeito")
    else:
        print(f"{n} nao eh perfeito")
