"""
d1 = {'chave1':'valor da chave'}
d1['nova_chave'] = 'Valor da nova chave'

print(d1)
"""

clientes = {
    'clientes1' : {
        'nome' : 'Luiz',
        'sobrenome' : 'Otavio',
    },
    'cliente2' : {
        'nome' : 'João',
        'sobrenome' : 'Moreira'
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
        