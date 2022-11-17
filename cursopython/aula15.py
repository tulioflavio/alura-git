"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
Enumerate - Enumerar elementos da lista # List / iteráveis

string = "O Brasil é o país do futebol, o Brasil é penta."
lista_1 = string.split(' ')
lista_2 = string.split(',')

palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')
"""

string = 'O Brasil é penta.'
lista = string.split(' ')
string2 = ' '.join(lista)

print(string)
print(lista)
print(string2)

lista = ['Luiz', 'Joao', 'Maria']

for indice, nome in enumerate(lista):
    print(indice, nome)
    



