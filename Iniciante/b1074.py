x = int(input())

for i in range(x):
    num = int(input())

    if num == 0:
        print("NULL")
    elif num % 2 == 0 and num > 0:
        print("EVEN POSITIVE")
    elif num % 2 == 0 and num < 0:
        print("EVEN NEGATIVE")
    elif num % 2 != 0 and num > 0:
        print("ODD POSITIVE")
    elif num % 2 != 0 and num < 0:
        print("ODD NEGATIVE")
    