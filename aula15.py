class Carro:
    #toda função dentro de classe são métodos
    #definindo atributos
    def __init__(self, proprietario, modelo, cor, preco, marca):
        #self = referência
        self.proprietario = proprietario  #criando variáveis e atribuindo atributos
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.marca = marca

    #função para retornar mensagem
    def __str__(self):
        return f'oi {self.proprietario}, seu carro é {self.modelo}, {self.cor} - {self.marca} valendo {self.preco}'

#instanciando a minha classe
meu_carro = Carro(
    #defuinindo valores aos meus atributos
    proprietario='Carlos',
    modelo='Fusca com cílios',
    cor='rosa',
    preco=90000000,
    marca='Ford'
)


print(meu_carro)
