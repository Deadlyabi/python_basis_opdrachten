def stel_vragen(vragen):
    antwoorden = {}

    for vraag in vragen:
        antwoord = input(f"{vraag}\n")
        antwoorden[vraag] = antwoord

    with open("feestgangers.txt", "a") as bestand:
        for vraag, antwoord in antwoorden.items():
            bestand.write(f"{vraag}: {antwoord}\n")
        bestand.write("\n")

    print("Bedankt voor het invullen!")
    print("See you at the party.")

# Lijst met vragen
vragenlijst = [
    "Wat is je voornaam?",
    "Wat is je achternaam?",
    "Wat neem je mee aan drank?",
    "Wat neem je mee om te eten?"
]

# Roep de functie aan om vragen te stellen en antwoorden op te slaan
stel_vragen(vragenlijst)
