def imprimir_dados(nome, idade=None):
    if idade is not None:
        print('nome: {}, idade: {}'.format(nome,idade))
    else:
        print('Nome: {}'.format(nome))


imprimir_dados('james')


def somar_numeros(n1, n2):
    soma = n1 + n2
    return soma


print(somar_numeros(10, 21))


def tirulos_copa_mundo(pais, *args):
    print('O país {}'.format(pais))
    print('Tem os seguintes títulos:')
    for titulo in args:
        print(titulo)

tirulos_copa_mundo('Brasil', '1994', '2000', '2002')

