class Funcionario:
    def __init__(self, nome, email, rg, idade, salario):
        self.nome = nome
        self.email = email
        self.rg = rg
        self.idade = idade
        self.salario = salario

    def __str__(self):
        return f'Olá {self.nome}, você foi cadastrado com sucesso em nosso sistema'

    def aumentar_salario(self, valor):
        return  self.salario + valor

cliente_criado = Funcionario(
    nome='Carlos',
    email='carlos@gmail.com',
    rg='90380983',
    idade=9,
    salario=2000
)

print(cliente_criado)
print(cliente_criado.aumentar_salario(float(input('Insira o aumento: '))))
