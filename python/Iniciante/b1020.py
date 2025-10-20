d = int(input())
a = d // 365
m = d % 365 // 30
d =  d % 365 % 30
print(f"{a} ano(s)")
print(f"{m} mes(es)")
print(f"{d} dia(s)")
