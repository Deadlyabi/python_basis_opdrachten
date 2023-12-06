def kies_topping(beschikbare_toppings):
    while True:
        keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings}\n").lower()
        
        for topping, prijs in toppings:
            if keuze == topping.lower():
                print(f"U heeft {topping} besteld. Dat kost {prijs}")
                return prijs
        
        print("Uw keuze zit niet in ons assortiment. Probeer het opnieuw.")


toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00), ("ansjovis", 2.50)]


beschikbare_toppings = [topping[0] for topping in toppings]

gekozen_topping = kies_topping(beschikbare_toppings)

