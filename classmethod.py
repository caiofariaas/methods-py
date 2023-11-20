# Estudo classmethod
# Através de uma class Pessoa vamos entender o uso de classmethod

class Pessoa:
    
# Aqui inicializamos um contador que será responsavel por armazenar o total de pessoas

    total_pessoas = 0
    
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
    
# Aqui definimos um contador para cada vez que uma instancia for criada a partir do método 'init'

        Pessoa.total_pessoas += 1
        
# Método criado para instancias
        
    def apresentar(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}")
        
# Método criado para ser um método da classe(classmethod)        

    @classmethod
    def contar_pessoas(cls):
        print(f'Pessoas Criadas: {cls.total_pessoas}')

# Criação dos objetos a partir da classe 'Pessoa'
        
pessoa1 = Pessoa("Caio", 18)
pessoa2 = Pessoa("Paulo", 40)
pessoa3 = Pessoa("Amanda", 30)

# Uso dos métodos criados para a instancia

pessoa1.apresentar()
pessoa2.apresentar()

# Uso do método criado para a classe!

Pessoa.contar_pessoas()

# A principal diferença entre um método de instância comum e um método de classe
# é que o primeiro recebe uma instância como seu primeiro argumento (self)
# enquanto o último recebe a classe como seu primeiro argumento (cls).


# Um segundo exemplo usando o classmethod para a criação de objetos!

class Circulo:
    def __init__(self, raio: float):
        self.raio = raio
        
# Criação do classmethod
        
    @classmethod
    def criar_circulo(cls, diametro):
            raio = diametro / 2
            
# Estamos usando cls para criar uma nova instância da classe à qual o método pertence.
# Neste caso, está sendo criada uma instância de círculo, 
# e o raio calculado é passado como argumento para o construtor (__init__) da classe.

            return cls(raio)
        
# Criação dos objetos
# O primeiro sendo criado através do método 'init'

circulo1 = Circulo(5)

# O segundo sendo criado a partir do classmethod 'criar_circulo()'

circulo2 = Circulo.criar_circulo(5)

print(circulo2.raio)
   
     