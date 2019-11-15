print('Ha quantos produtos diferentes na cesta?')
prod = int(input())
i = prod
j = 0
total_quant = 0
total_preco = 0
total = 0

quantidades = []
nomes = []
precos = []

while prod > 0:
    nomes.append(input('Nome: '))
    quantidades.append(int(input('Quantidade: ')))
    precos.append(float(input('Preço: ')))
# miau
    prod -= 1

while j < i:
    print('{} . Quantidade: {}  |  Nome: {}  |  Preço: {}'.format(j + 1, quantidades[j], nomes[j], precos[j]))
    total_quant = quantidades[j]
    total_preco = precos[j]
    total += total_quant * total_preco

    j += 1

print('Total da compra: {}'.format(total))
