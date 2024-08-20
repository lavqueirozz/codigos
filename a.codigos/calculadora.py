# pokemon
class Pokemon:
    def __init__(self,nome,level,hp,genero,desbloqueio):
        self.nome = nome
        self.level = level
        self.hp = hp
        self.genero = genero
        self.desbloqueio = desbloqueio

        Pikachu = Pokemon('Pikachu','level 20','45/45','Masculino','Ativo')
        Pidgeotto = Pokemon('Pidgeotto', 'level 20','57/57', 'Masculino', 'Desativado')

        def menu_escolha():
            print('-Pikachu')
        print ('-Pidgeotto')

        def Escolha():
         menu_escolha()
        escolha = input('Escolha seu Pokemon')
        if escolha == ('Pikachu'):
                print(Pikachu.nome, Pikachu.level, Pikachu.hp, Pikachu.genero, Pikachu.desbloqueio)
        elif escolha == ('Pidgeotto'):
            print(Pidgeotto.nome, Pidgeotto.level, Pidgeotto.hp, Pidgeotto.genero, Pidgeotto.desbloqueio)
        else:
            print('this pokemon dont exist')

            escolha ()
       

    






