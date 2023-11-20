# Estudo staticmethod
# staticmethod's não possuem acesso aos atributos de uma classe, ele não pode receber 'self' ou 'cls' como parametro!
# também não são acessados a partir de instancias de classe, são acessados apenas pela classe em sí.
import math

class Calculadora:

# Criação de dois staticmethod's

    @staticmethod
    def somar(a, b):
        return a + b
    
    @staticmethod
    def subtrair(a, b):
        return a - b
    
# Aqui um exemplo de seu uso
    
result = Calculadora.somar(10, 20)

print(f'{result}\n')

# Neste segundo exemplo vamos criar uma classe 'Usuario'

class Usuario:
    def __init__(self, nome: str, idade: int, senha: str):
        
# Inicializando os atributos da classe

        self.nome = nome
        self.idade = idade
        self.senha = senha
        
# Aqui vamos criar um staticmethod que verifica se a senha digitada por um usuário é válida!

    @staticmethod
    def validar(senha):
        if len(senha) >= 8:
            return "\nSenha criada com sucesso!\n"
        else:
            return "\nSenha inválida! crie uma senha com no mínimo 8 caracteres.\n"
        
# Pedimos a entrada do usuário, neste caso a Senha
        
senha = input("Digite uma senha de no mínimo 8 caracteres: ")

# E aqui chamados o método a partir da classe e passando como parametro a variável responsável por armazenar a senha!

print(Usuario.validar(senha))

# Agora o ultimo exemplo de staticmethod
# Calculadora

class Matematica:
    
# O método a seguir seria responsável por dizer se o número digitado é par ou não
# Ele irá retornar 'true' ou 'false'
    
    @staticmethod
    def eh_par(num):
        return num % 2 == 0
    
num = float(input("Digite um número: "))
    
if Matematica.eh_par(num):
    print("\nÉ par\n")
else:
    print("\nÉ impar\n")

# Conclusão, staticmethod's não tem acesso aos atributos de uma classe
# em sua maioria são usados para verificações 
# Ou apenas para uma classe de funções