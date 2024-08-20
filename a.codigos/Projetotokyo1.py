class ControleRemoto:
    def __init__(self, cor, altura,largura,profundidade):
        self.cor = cor 
        self.altura = altura
        self.largura = largura 
        self.profundidade = profundidade

    def Passar_Canal(self, botao):
        if botao == '+':
            print('Aumentar Volume')
        elif botao == '-':
            print('Diminuir Volume')
        
Controle_Remoto1 = ControleRemoto('preto', '120cm', '115', '10cm') 
print(Controle_Remoto1.cor)
Controle_Remoto1.Passar_Canal('+')

Controle_Remoto2 = ControleRemoto('cinza', '120cm','115cm', '10cm')
