salBruto = float(input('Insira o salário bruto: '))

inss = 0.09 * salBruto
valeTrans = 0.03 * salBruto
planSaude = 0.15 * 347

salLiq = salBruto - inss - valeTrans - planSaude

print('O salário bruto é {}'.format(salBruto))
print('O valor descontado do INSS (9%) é {}'.format(inss))
print('O valor descontado do vale transporte (3%) é {}'.format(valeTrans))
print('O valor descontado do Plano de saúde (15% de 347) é {}'.format(planSaude))
print('O salário Liquído é {}'.format(salLiq))
