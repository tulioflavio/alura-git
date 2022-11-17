"""
Operadores Relacionais
== > >= < <= !=
"""
nome = input(' qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)

#Limite para pegar empréstimo
idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar o empréstimo. ')
else:
    print(f'{nome} NÃO pode pegar o empréstimo. ')
    
