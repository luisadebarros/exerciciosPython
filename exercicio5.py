prod = input('Há produtos no carrinho? (sim) (nao)')
if prod == 'sim' or prod == 'nao':
    while prod == 'sim':
        print('Qual a quantidade do produto?')
        quant = [int(input())]
        print('Qual o produto?')
        nome = input()
        print('Qual o preço do produto? R$')
        preco = float(input())
        prod = input('Há produtos no carrinho? (sim) (nao)')

    print(quant[0])

else:
    print('Erro 404 (insira somente (sim) ou (nao) ESPECIFICAMENTE, sem parenteses)')
