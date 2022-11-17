"""
while em python
utilizado para realizar ações enquanto uma condição for verdadeira
Requisitos: entender condições e operadores

while True:
    nome = input("QUal o seu nome? ")
    print(f'Olá {nome}!')

x = 0
while x < 100:
    print(x)
    x = x + 1

print('Acabou')

x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue

    print(x)
    x = x + 1

print("Acabou!")

x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break

    print(x)
    x = x + 1

print("Acabou!")
"""

x = 0 #coluna
while x < 10:
    y = 0 ##linha

    while y < 5:
        print(f'({x},{y})')
        y = y + 1

    x = x + 1 #x += 1

print('Acabou!')
