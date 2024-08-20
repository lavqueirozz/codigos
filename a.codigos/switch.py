cardapio_frutas = ['1-banana','2-morango','3-abacaxi','4-manga']
print(cardapio_frutas)

fruta = input('Escolha uma fruta do cardapio a cima:')

match fruta:
    case '1':
        print ('Vitamina de Banana')
    case '2':
        print('Suco de morango')
    case '3':
        print('Suco de abacaxi')
    case '4:':
        print('Suco de manga')
    case _:
        print('Esta fruta não esta disponivel')

while fruta != cardapio_frutas:
    print(fruta)