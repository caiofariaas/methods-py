# Estudo polimorfismo
# Só continue aqui caso ja tenha visto as aulas de herança!

# O polimorfismo permite que declaremos métodos com o mesmo nome em diversas classes diferentes
# Pense como uma sobreposição de métodos
# Um exemplo que esta sendo mostrado agora é que a classe 'Veiculo' possui um método chamado mover e um chamado barulho
# e vemos que as classes Bicicleta e Carro também possuem métodos com o mesmo nome

class Veiculo:
    
# Métodos

    def mover(self):
        pass
    
    def barulho(self):
        pass
    
# Classe Carro herda de 'Veiculo'
    
class Carro(Veiculo):
    
    def mover(self):
        return "\nCarro em movimento!\n"
    
    def barulho(self):
        return "\nVruum Vruum\n"
    
# Classe Bicicleta herda de 'Veiculo'
    
class Bicicleta(Veiculo):
    
# Métodos
    
    def mover(self):
        return "\nBike em movimento\n"
    
    def barulho(self):
        return "\nPlin Plin\n"
    
# Aqui testamos o poliformismo
# Ocorre uma especie de sobreposição de métodos, sendo as classes filhas, mais especificas!!

# Criação dos Objetos e Teste

carro = Carro()
bike = Bicicleta()

print(carro.barulho())
print(bike.barulho())
