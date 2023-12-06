def enquete():
    antwoorden = []

    vraag1 = input("Wat vind je van de huidige regering?\n")
    antwoorden.append(f"1. Wat vind je van de huidige regering? {vraag1}\n")

    vraag2 = input("Wat vind je van de Python-lessen tot nu toe?\n")
    antwoorden.append(f"2. Wat vind je van de Python-lessen tot nu toe? {vraag2}\n")

    vraag3 = input("Wat vind jij de mooiste stad van Nederland?\n")
    antwoorden.append(f"3. Wat vind jij de mooiste stad van Nederland? {vraag3}\n")

    with open("enquete_resultaten.txt", "w") as bestand:
        bestand.writelines(antwoorden)
    
    print("Bedankt voor het invullen van de enquête. De resultaten zijn opgeslagen in 'enquete_resultaten.txt'.")


enquete()