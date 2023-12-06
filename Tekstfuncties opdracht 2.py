Voornaam = "Ufuk"
Achternaam = "Demirel"
Groep = "Deltion"

my_list = [Voornaam, Achternaam, Groep]

gecombineerde_tekst = " ".join(my_list)

aantal_keer_t = gecombineerde_tekst.count("t")

print(f"Het aantal keren dat de letter 't' voorkomt is: {aantal_keer_t}")
