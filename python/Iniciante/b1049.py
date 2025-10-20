classe = input()
familia = input()
alimentacao = input()

if classe == "vertebrado" and familia == "ave" and alimentacao == "carnivoro":
    print("aguia")
elif classe == "vertebrado" and familia == "ave" and alimentacao == "onivoro":
    print("pomba")
elif classe == "vertebrado" and familia == "mamifero" and alimentacao == "onivoro":
    print("homem")
elif classe == "vertebrado" and familia == "mamifero" and alimentacao == "herbivoro":
    print("vaca")#esse n funciona
elif classe == "invertebrado" and familia == "inseto" and alimentacao == "hematofago":
    print("pulga")
elif classe == "invertebrado" and familia == "inseto" and alimentacao == "herbivoro":
    print("lagarta")
elif classe == "invertebrado" and familia == "anelideo" and alimentacao == "hematofago":
    print("sanguessuga")
elif classe == "invertebrado" and familia == "anelideo" and alimentacao == "onivoro":
    print("minhoca")