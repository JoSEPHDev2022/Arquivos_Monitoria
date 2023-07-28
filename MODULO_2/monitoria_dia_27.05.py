class Estudante:

    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota
    
    def get_name(self):
        return self.nome
    
    def get_age(self):
        return self.idade
    
    def get_grade(self):
        return self.nota
    
    def set_name(self, nome):
        self.nome = nome
    
    def set_age(self, idade):
        self.idade = idade
    
    def set_grade(self, nota):
        self.nota = nota
    
    def check_dados(self):
        mensagem_erro = []
        
        if not isinstance(self.nome, str) or len(self.nome) == 0:
            mensagem_erro.append("Nome inválido!")
        
        if not isinstance(self.idade, int) or self.idade <= 0:
            mensagem_erro.append("Idade inválida!")
        
        if not isinstance(self.nota, float) or (self.nota < 0 or self.nota > 10):
            mensagem_erro.append("Nota inválida!")
        
        if mensagem_erro:
            return mensagem_erro
        else:
            return "Dados válidos!"

estudante_1 = Estudante("João", 18, 9.5)
# print(estudante_1.check_dados())  

# estudante_2 = Estudante("Maria", "20", 11)
# print(estudante_2.check_dados()) 

# print(estudante_1.get_age())
# estudante_1.set_age(19)
# print(estudante_1.get_age())