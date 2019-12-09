nome = str(input('Digite o nome completo: '))
idade = int(input('Digite o saldo a sua idade: '))
saldo = int(input('Digite o saldo da sua conta:'))

print(f'Digite o número desejado: \n', 
      f'Digite (1) para saque \n',
      f'Digite (2) para depósito \n',
      f'Digite (3) para empréstimo \n',
      f'Digite (4) para visualizar informações \n',
      f'Digite (Qualquer outro texto ou número) para sair')
conta = int(input(''))

def saque(valor, saldo):
    if saldo > valor >= 1000 or saldo > valor:
        saldo = saldo - valor
        print(saldo)
    else:
        print('Saldo insuficiente')

def deposito(valor, saldo):
    if valor == 5000:
        print('Valor alto de mais')
    else:
        saldo = saldo + valor
        print(saldo)

def emprestimo(valor, saldo, idade):
    if conta == 3:
        if idade > 21 and saldo >= 1000 and 15 * saldo > valor > 2000:
            saldo = saldo + valor
            print(saldo)
        else:
            print('Não foi possível realizar o empréstimo')

if conta == 1:
    saque(int(input('Qual o valor a ser sacado: ')), saldo)

if conta == 2:
    deposito(int(input('Qual o valor do depósito: ')), saldo)

if conta == 3:
    emprestimo(int(input('Digite o valor do empréstimo: ')), saldo, idade)

if conta == 4:
    print(f'Nome: {nome} \n Idade: {idade} \n Saldo:{saldo}')