i = 0.0

while i <= 2.0:
    for j in range(1, 4):
        valor_j = i + j
        if round(i, 1).is_integer():
            print(f"I={int(round(i, 1))} J={int(round(valor_j, 1))}")
        else:
            print(f"I={round(i, 1):.1f} J={round(valor_j, 1):.1f}")
    i = round(i + 0.2, 1)
