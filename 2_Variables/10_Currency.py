pesos = int(input('What do you have left in pesos?'))
soles = int(input('What do you have left in soles?'))
reais = int(input('What do you have left in reais?'))

pesos_dollar = pesos * 0.00025
soles_dollar = soles * 0.28
reais_dollar = reais * 0.18

total = pesos_dollar + soles_dollar + reais_dollar

print(total)
