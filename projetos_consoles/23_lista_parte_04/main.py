cidades =['Porto Alegre',
    'Gramado',
    'Miamar',
    'Curitiba',
    'Dallas',
    'Novo Horizonte',
    'Porto Alegre',
    'Gramado',
    'Miamar',
    'Curitiba',
    'Dallas',
    'Novo Horizonte',
    'Dallas',
    'Novo Horizonte',
    'Dallas',
    'Novo Horizonte'
    
]

cidade_pesquisada = input('Informe a cidade a ser pesquisada: ').title().strip()

qtde = cidades.count(cidade_pesquisada)

print(f'{cidade_pesquisada} foi encontrado {qtde} vezes na lista.')