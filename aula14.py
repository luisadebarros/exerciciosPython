import math

pessoa = {
    'nome': 'Groger',
    'CPF': '8912891478',
    'idade': 74,
    'email': 'matfd.2002@gmail.com'
}

print('Ola {}, esse é seu email: {}'.format(pessoa['nome'], pessoa['email']))

pessoa.update({'está trabalhando': True})

print(pessoa)

salada_de_frutas = ('kiwi', 'tomade', 'maionese', 'abacate', 'abacate', 'kiwi')

print(salada_de_frutas.count('abacate'))


def soma(a, b):
    soma = a + b
    return soma


print(soma(1, 2))

x = 64
print(x.__pow__(2))
print(x.__mod__(2))
print(x.__add__(2))

