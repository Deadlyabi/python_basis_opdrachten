normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

leeftijd_input = int(input("Geef uw leeftijd in aantal jaar: "))

groep = ""
for key, value in leeftijd.items():
    if value[0] <= leeftijd_input <= value[1]:
        groep = key
        break

if groep not in kortings_percentages:
    print(f"Error: Geen kortingspercentage gevonden voor de groep {groep}")
else:
    
    korting_percentage = kortings_percentages[groep]
    korting_bedrag = normale_toegangsprijs * (korting_percentage / 100)
    aangepaste_prijs = normale_toegangsprijs - korting_bedrag

    print(f"U behoort tot de groep {groep}")
    print(f"U krijgt {korting_percentage}% korting")
    print(f"U betaalt daarom {aangepaste_prijs:.2f}")

