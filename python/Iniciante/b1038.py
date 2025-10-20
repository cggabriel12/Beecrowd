x , y = input().split()
x = int(x)
y = int(y)

if x == 1:
    print(f"Total: R$ {y * 4:.2f}")
elif x == 2:
    print(f"Total: R$ {y * 4.5:.2f}")
elif x == 3:
    print(f"Total: R$ {y * 5:.2f}")
elif x == 4:
    print(f"Total: R$ {y * 2:.2f}")
elif x == 5:
    print(f"Total: R$ {y * 1.5:.2f}")