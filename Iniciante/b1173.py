num = []

num.append(int(input()))

for i in range(9):
    num.append(num[i] * 2)

for i in range(10):
    print(f"N[{i}] = {num[i]}")
