while True:
    try:
        n = int(input())
        r = 0
        for i in range(1,n+1):
            r = (r * 10 + 1) % n
            if r == 0:
                print(i)
                break



    except EOFError:
        break
