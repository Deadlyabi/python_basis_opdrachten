getallen_lijst = []

for num in range(1, 11): 
    getallen_lijst.append(num)

resultaat_lijst = [getal for getal in getallen_lijst if getal > 4]

print(resultaat_lijst)