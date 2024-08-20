# Viagens
idadePermitida = int(input('Informe sua idade:'))
# if idadePermitida >= 18:
#     print(True)
    
# else:
#     print ( False)
vistoPermitido = '511.348.058.45'
Visto = input('Informe o numero do seu visto:')

# if Visto == vistoPermitido:
#     print  (True)
# else:
#     print(False) 

if (idadePermitida >= 18) or (Visto == vistoPermitido):
    print(True, 'Acesso liberado')
elif (idadePermitida <18 ) or (Visto != vistoPermitido):
    print(False,'Acesso negado')












