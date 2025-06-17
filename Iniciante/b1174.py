num = []

for i in range(100):
    num.append(float(input()))

for i in range(100):
    if num[i] <= 10:
        print(f"A[{i}] = {num[i]}")

