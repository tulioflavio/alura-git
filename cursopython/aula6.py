"""
Entrada de dados
"""
from telnetlib import STATUS


nome = input("Qual o seu nome? ")
print(f'O usuário digitou {nome} e o tipo de variável é '
f'{type(nome)}' )
