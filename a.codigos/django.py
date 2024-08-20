class pessoas:
    def __init__(self,nome,cpf,tel):
        self.nome = nome
        self.cpf = cpf
        self.tel = tel

    nome = input('informe seu nome:')
    cpf = float(input('informe seu cpf'))
    tel = int(input('informe seu numero de telefone'))

pessoa1 = pessoas (nome, cpf, tel)

