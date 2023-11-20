# Apenas continue aqui se ja viu o arquivo Animal.py!
# Vamos entender melhor a questão do acesso aos atrbutos!

# Classe pai

class Animal:
    def __init__(self, nome, cor):
        
# Atributos

        self.nome = nome
        self.cor = cor
        
# Métodos        

    def apresentar(self):
        return f'olá meu nome é {self.nome}'
    
# Classe Filha
# Repare que temos um 'super' dentro do nosso construtor
# nesse contexto, o super é responsável por buscar atributos da classe Pai 'Animal'

class Cachorro(Animal):
    def __init__(self, nome, cor, raca):
        
# Super esta puxando os atributos 'nome' e 'tipo' do método '__init__'  presente na classe Pai
# Dessa forma, temos os atributos da classe pai e caso necessário é possivel criar mais atributos para a classe Filha.
# assim como no exemplo: 
        
        super().__init__(nome, cor)
        self.raca = raca
        
# Métodos
# No primeiro método, conservamos o método 'apresentar' da classe pai
# Atribuindo o valor dela a uma variável
# e depois a complementamos com mais uma informação que não era presente lá.

# Repare também que fizemos uma sobreposição de métodos
# Isto é, o método 'apresentar' de Cachorro fornece algo especifico também!

    def apresentar(self):
        
        apresentacao_class_pai = super().apresentar()
        
        return f'{apresentacao_class_pai} e sou da raça {self.raca}!'
    
# Criação do objeto

cachorro = Cachorro("Buddy", "Caramelo", "Vira-lata")

print(cachorro.apresentar())
