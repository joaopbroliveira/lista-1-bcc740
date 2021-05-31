class Pessoa: 
    def __init__(self, name):
        self.nome = name
    def __str__(self): 
        return self.name

joao = Pessoa("Joao")
print(joao)
pedro = Pessoa("Pedro")
print(pedro)
print(Pessoa("Oliveira"))
