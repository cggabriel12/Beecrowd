dia1 = int(input())
hora1 , minuto1 , segundo1 = map(int , input().split(" : "))
dia2 = int(input())
hora2 , minuto2 , segundo2 = map(int , input().split(" : "))

tempo1 = ((dia1 * 24) * 3600) + (hora1 * 3600) + (minuto1 * 60) + segundo1
tempo2 = ((dia2 * 24) * 3600) + (hora2 * 3600) + (minuto2 * 60) + segundo2

duracao = tempo2 - tempo1

diat = duracao // 86400
horat = (duracao % 86400) // 3600
minutot = duracao % 3600 // 60
segundot = duracao % 3600 % 60

print(f"{diat} dia(s)")
print(f"{horat} hora(s)")
print(f"{minutot} minuto(s)")
print(f"{segundot} segundo(s)")