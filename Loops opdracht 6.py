pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

pizzas.sort()
print(pizzas)

pizzas.append('Pizza tonijn')
print(pizzas)

pizzas.remove('verdi')

print(pizzas[:3])

print(pizzas[len(pizzas)//2])

print(pizzas[-3:])