i = 0
j = 0
acumulador = 0
lista_notas = []

while i < 4:
    print('Digite a nota {} :'.format(i + 1))
    lista_notas.append(int(input()))
    i += 1

i = 0
while i < 4:
    acumulador += lista_notas[i]
    i += 1

media = acumulador / i

if media >= 7:
    print('Parabéns, você foi aprovado ({})'.format(media))
elif 7 > media >= 5.5:
    print('Recuperação! ({})'.format(media))
else:
    print('Reprovado! ({})'.format(media))
