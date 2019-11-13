n1 = int(input('Insira a primeira nota: '))
n2 = int(input('Insira a segunda nota: '))
n3 = int(input('Insira a terceira nota: '))
n4 = int(input('Insira a quarta nota: '))

media = (n1 + n2 + n3 + n4) / 4

if media > 7:
    print('Parabéns, você foi aprovado ({})'.format(media))
elif 7 > media > 5.5:
    print('Recuperação! ({})'.format(media))
else:
    print('Reprovado! ({})'.format(media))
