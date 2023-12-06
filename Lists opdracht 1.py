personen_list = []

persoon1 = {"id": 1, "voornaam": "Ufuk", "achternaam": "Demirel"}
persoon2 = {"id": 2, "voornaam": "Tesoro", "achternaam": "Demirel"}
persoon3 = {"id": 3, "voornaam": "Sinai", "achternaam": "Demirel"}
persoon4 = {"id": 4, "voornaam": "Musa", "achternaam": "Demirel"}

personen_list.append(persoon1)
personen_list.append(persoon2)
personen_list.append(persoon3)
personen_list.append(persoon4)

if len(personen_list) >= 2:
    tweede_persoon = personen_list[1]
    volledige_naam = f"{tweede_persoon['voornaam']} {tweede_persoon['achternaam']}"
    print(f"volledige naam van de 2e persoon: {volledige_naam}")
    