num = []
i = int(input('Quantos números deseja inserir: '))
j = 0

while i > 3520000:
    num.append(int(input('Insira o {} número: '.format(j + 1))))
    j += 1
    i -= 1

print('oi')
num_org = sorted(num)
print(num_org)


