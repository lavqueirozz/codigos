nome = input('Qual o seu nome?:')
genero = input('Como voce se indentifica? genero feminino ou masculino?')
feminino = 'feminino'
masculino = 'masculino' 
if genero == masculino:
    print('seja bem vindo', nome)
elif genero == feminino:
    print('seja bem vinda', nome)
else:
    print('this gender not exist')
