  
nota1 = float(input('digite um primeiro numero:'))
if nota1 >10:
    print('digite um numero valido')
elif nota1 <0:
    print('por favor,escolha um numero valido')

nota2 = float(input('digite um segundo numero:'))

if nota2 >10:
      print('digite um numero valido')
elif nota2 <0:
      print('por favor digite um numero valido')
      
# if nota1 and nota2 <10:
#      soma = nota1 + nota2
# elif nota1 and nota2 >0:
#      soma = nota1 + nota2
# else:
#      print('algo deu errado')
soma = nota1 + nota2
resultado = soma/2
print('resultado:', resultado)
if resultado >= 6.0:
      print('voce passou!')
else:
      print('voce ficou retido')