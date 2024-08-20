#clientes netflix

class Clientes:
    def __init__(self,nome, cpf, aniversario, cidade, estado, email,senha,):
        self.email = email
        self.senha = senha
        self.nome = nome
        self.cpf = cpf
        self.aniversario = aniversario
        self.cidade = cidade
        self.estado = estado
    




Clientes_1 = Clientes 
print(Clientes_1.nome)
print(Clientes_1.cpf)
print(Clientes_1.aniversario)
print(Clientes_1.cidade)
print(Clientes_1.estado)
print(Clientes_1.email)
print(Clientes_1.senha)

# Clientes_2 = Clientes ('xxxxxxxs','000.000.000-00','05/06/1980','São Paulo', 'SP', 'xxxxxxxx@hotmail.com', '4546678')
# print(Clientes_2.nome)
# print(Clientes_2.cpf)
# print(Clientes_2.aniversario)
# print(Clientes_2.cidade)
# print(Clientes_2.estado)
# print(Clientes_2.email)
# print(Clientes_2.senha)