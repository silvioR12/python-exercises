"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;

"""
import os
clear = lambda: os.system('clear')
clear()



def inverter(txt):
  return txt[::-1]

texto = input('Digite uma palavra: ')
texto_invertido = inverter(texto)

clear()
print('Normal:  {} '.format(texto))
print('Texto invertido: {} '.format(texto_invertido))