"""
Formatando valores
:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:. (NÚMERO) f - Quantidade de casas decimais (float)
: (CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print( f'{divisao:.4f}' )

nome = 'Tulio Flavio'
nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)

nome = 'Túlio Vasconcellos'
print(nome.lower())
print(nome.upper())
print(nome.title())
