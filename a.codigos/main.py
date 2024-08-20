
from conda import math

def soma (a, b):
    return a + b
def subtração (a, b):
    return a - b 
def multiplicação (a, b):
    return a * b 
def divisão (a,b):
    return a / b

def exibir_menu():
  print('1-soma')
  print('2-subtração')
  print('3-multiplicação')
  print('4-divisão')

def calcular():
  exibir_menu()
  operação = input('Digite o numero da operação desejada')
  num1 = float(input('Digite um numero'))
  num2 = float(input('Digite outro numero'))
  if operação == '1-soma':
    resultado = soma (num1, num2)
  elif operação == '2-subtração':
    resultado = subtração (num1, num2)
  elif operação == '3-multiplicação':
    resultado = multiplicação (num1, num2)
  elif operação == '4-divisão':
    resultado = divisão (num1, num2)
  else:
    print('operação invalida')
    return 
  print('O resultado é:', resultado) 
  calcular()