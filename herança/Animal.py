# Estudo herança de classes
# Primeiro vamos criar duas classes, uma classe 'Animal' e uma 'Cachorro'
# Onde cachorro herdará de Animal!

# Animal será oque chamamos de classe Pai

class Animal:
    def __init__(self, nome):
        self.nome = nome
        
# Aqui criamos um método que permite algum objeto criado através da classe animal se apresentar!       

    def apresentar(self):
        return f'olá meu nome é {self.nome}!'
    
    
# Cachorro será a classe filha!
# A classe Cachorro esta herdando de Animal
# com isso é possivel que os objetos instanciados a partir da classe cahorro
# também tenham acesso aos métodos da classe Animal!

class Cachorro(Animal):
    
    def fazer_som(self):
        return 'Au Au'
    
# Criação do objeto
# Repare que na criação do objeto utilizamos o mesmo construtor da classe 'Animal'

cachorro = Cachorro("Buddy")

# Acesso ao método da classe 'Animal' através de um objeto criado pela classe 'Cachorro'!

print(cachorro.apresentar())

# Mas e se caso a classe filha tiver atributos que a classe pai não tem?
# Vamos falar mais sobre isso no arquivo Animal2.py presente na pasta 'Herança'
