# Estudo property
# O property é usado para transformar um método em uma propriedade
# permitindo que você  acesse e modifique um atributo de maneira controlada
# como se fosse um atributo de instancia mas tambem seria possivel inserir alguma lógica!
# Exemplo: 

class Usuario:
    def __init__(self):
        self.__senha = None
        
# Sabemos que o property da a possibilidade de criarmos diversos métodos com o mesmo nome
# porem, com lógicas diferentes
# nos exemplos a seguir criamos 3 métodos com o mesmo nome, entretanto, um apenas retornará a senha
# o outro é um 'setter' ou seja, ele definirá qual sera a nova senha baseada em uma entrada do usuário
# e por ultimo um método para deletar esse Atributo!
        
    @property
    def minha_senha(self):
        return self.__senha
    
    @minha_senha.setter
    def minha_senha(self, senha):
        self.__senha = senha
        
    @minha_senha.deleter
    def minha_senha(self):
        del self.__senha
        
# Criação do objeto

senha = Usuario()

# Aqui estamos usando o método como um 'setter'!

senha.minha_senha = "Caio123"

# Aqui usamos ele como um 'getter'!

print(senha.minha_senha)

# E aqui usamos ele como um deleter

del senha.minha_senha

# e na hora que rodamos novamente um getter, ele apresentará um erro 'AttributeError'
# isso acontece porque acabamos de deletar este atributo!
# ele está comentado para que não quebre por enquanto, mas faça o teste!

# print(senha.minha_senha)

# Segundo exemplo

class Circulo:
    def __init__(self):
        self.__raio = None
        
# Neste exemplo usamos o property para que possamos utilizar o mesmo nome de método para executar duas funções
# o primeiro sendo um 'getter' e o segundo sendo um 'setter'
        
    @property
    def raio(self):
        return self.__raio
    
    @raio.setter
    def raio(self, raio):
        self.__raio = raio
        
# Exemplo de uso
# Criação do objeto

circulo = Circulo()

# Uso do método 'raio' como 'setter'

circulo.raio = 10

# Uso do método 'raio' como 'getter'

print(circulo.raio)
