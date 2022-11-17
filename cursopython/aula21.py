"""
Funções (def) em Python - *args **kwargs
"""

def func(*args):
    print(args)

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2)

def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'])

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome='Luiz')

