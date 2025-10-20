inicio_hora , inicio_minuto , fim_hora , fim_minuto = input().split()
inicio_hora = int(inicio_hora)
inicio_minuto = int(inicio_minuto)
fim_hora = int(fim_hora)
fim_minuto = int(fim_minuto)

tempo_inicio = (inicio_hora * 3600) + (inicio_minuto * 60)
tempo_fim = (fim_hora * 3600) + (fim_minuto * 60)

if tempo_inicio < tempo_fim:
    duracao = tempo_fim - tempo_inicio
    duracao_hora = duracao // 3600
    duracao_minuto = duracao % 3600 // 60
    print(f"O JOGO DUROU {duracao_hora} HORA(S) E {duracao_minuto} MINUTO(S)")

elif tempo_inicio == tempo_fim:
    print (f"O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

else:
     duracao = 86400 - tempo_inicio + tempo_fim
     duracao_hora = duracao // 3600
     duracao_minuto = duracao % 3600 // 60
     print(f"O JOGO DUROU {duracao_hora} HORA(S) E {duracao_minuto} MINUTO(S)")

