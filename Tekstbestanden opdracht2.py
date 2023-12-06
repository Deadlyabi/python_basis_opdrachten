import random

def raad_het_getal():
    geheime_getal = random.randint(1, 100)
    aantal_pogingen = 0

    print("Raad mijn geheime getal tussen 1 en 100.")

    while True:
        gok = int(input())
        aantal_pogingen += 1

        if gok < geheime_getal:
            print("hoger")
        elif gok > geheime_getal:
            print("lager")
        else:
            print(f"Je hebt het getal geraden, het is {geheime_getal}!")
            print(f"Je hebt het in {aantal_pogingen} keer geraden.")
            break


raad_het_getal()
