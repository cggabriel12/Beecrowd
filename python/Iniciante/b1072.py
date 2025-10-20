in_ = 0
out = 0

N =int(input())

for i in range(N):
    num = int(input())
    if 10 <= num and num <= 20:
        in_ += 1
    else:
        out += 1
print(f"{in_} in")
print(f"{out} out")