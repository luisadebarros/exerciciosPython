salbruto = float(input('Insira o salário bruto: '))


def calcular_inss():
    inss = 0.09 * salbruto
    return inss


inss = calcular_inss()


def calcular_valeTrans():
    vale = 0.03 * salbruto
    return vale


vale = calcular_valeTrans()


def calcular_plansaude():
    saude = 0.03 * salbruto
    return saude


saude = calcular_plansaude()


def calcular_salliquido():
    salLiq = salbruto - inss - vale - saude
    return salLiq


salLiq = calcular_salliquido()

print('O salário bruto é {}'.format(salbruto))
print('O valor descontado do INSS (9%) é {}'.format(inss))
print('O valor descontado do vale transporte (3%) é {}'.format(vale))
print('O valor descontado do Plano de saúde (15% de 347) é {}'.format(saude))
print('O salário Liquído é {}'.format(salLiq))
