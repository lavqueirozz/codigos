# tela inicio
print('Ola seja bem vindo(a) ao decolar.net')
# tela cadastro
nome = input("Nome:")
email = input('email:')
cpf = input("CPF:")
tel = input('seu numero de telefone:')
senha = input('informe uma senha de seis digitos:')
cadastro = email,senha,cpf,tel
print("Cadastro feito com sucesso!")

# escolher loc
print("\f Qual seu destino?")

estadosBR = (( 'Rio de Janeiro'),('São Paulo'),('Pernambuco'),('Bahia'),('Alagoas'),('Mato Grosso'))

cidadesBR = {'Rio de janeiro': ['arraial do cabo', 'Rio de janeiro'],'São Paulo':['Ribeirão Preto','São Paulo'],'Pernambuco':['Fernando de Noronha', 'Recife'],'Bahia':['Salvador','Canarana'],'Alagoas':['Maceió','Penedo'],"Mato Grosso": ['cuiabá','Várzea Grande']}

estado = input('Estado:')
cidade = input('Cidade:')
preco = 500
data = input('Escolha a data:')
passagem = (estado,cidade,data,preco)
if estado in cidadesBR and cidade in cidadesBR[estado]:
    print("Passagem adicionada ao carrinho:", passagem)
else:
    print("Essa passagem não esta disponivel, escolha uma valida!")

# efetuarpagamento
pagamento = input('Quer efetuar o Pagamento?')
if pagamento == '':
    print('Vamos efetuar o pagamento aguarde um momento')
else:
    print("OK")
formasDepagamento = ("PIX",'Cartão de débito','Cartão de Credito','Boleto')
print(formasDepagamento)
pagar = input('Escolha sua forma de pagamento:')
match pagar:
    case'PIX':
        print('11930746625','este é meu codigo PIX voce tem 30 minutos para efetuar o pagamento')
        print('\f', nome,"compra no PIX efetuada com sucesso, Boa Viagem!",passagem)
    case 'Cartão de débito':
        print("\f insira os dados do cartão")
        print(nome, 'Compra efetuada com sucesso, Boa Viagem!', passagem)
    case 'Cartão de credito':
        print(nome, 'Compra efetuada com sucesso, Boa Viagem!', passagem )
    case 'Boleto':
        print('\f', nome, "Boleto gerado, compra efetuada com sucesso, Boa Viagem!", passagem)
    case _:
        print('Escolha uma forma de pagamento valida')
    
    






