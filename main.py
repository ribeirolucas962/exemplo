#declarando as listas cazias
cardapio = []
comida = []

#pedindo para o usuário fornecer os valores

for c in range(0,4):
    comida.append ( str(input('Fale o nome do lanche:')))
    comida.append ( float(input('Fale o valor da comida:')))
    cardapio.append (comida[:])
    comida.clear()


test = "jhon"

print(cardapio)



