print('Insira o peso:')
peso = float(input(''))
print('Insira a altura:')
altura = float(input(''))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Peso: {}, Altura: {}, Imc: {}, você está abaixo do peso ideal'.format(peso, altura, imc))
elif imc <= 24.9:
    print('Peso: {}, Altura: {}, Imc: {}, peso normal'.format(peso, altura, imc))
elif imc <= 30:
    print('Peso: {}, Altura: {}, Imc: {}, acima do peso'.format(peso, altura, imc))
elif imc > 30:
    print('Peso: {}, Altura: {}, Imc: {}, você está obeso'.format(peso, altura, imc))