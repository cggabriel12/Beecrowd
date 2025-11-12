C = int(input())

for _ in range(C):
    N, M = map(int, input().split())
    radares = (N + M - 1) // M
    print(radares)
