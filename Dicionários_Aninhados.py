# Sistema simples de estacionamento usando dicionários

estacionamento = {
    'a1': {
        'marca': 'toyota',
        'modelo': 'corolla',
        'dono': 'sr. silva'
    },
    'b2': {
        'marca': 'honda',
        'modelo': 'civic',
        'dono': 'dona maria'
    },
    'c3': {
        'marca': 'ford',
        'modelo': 'mustang',
        'dono': 'sr. silva'
    }
}

# Acessando informação
print("Modelo na vaga b2:", estacionamento['b2']['modelo'])

# Alterando dado
estacionamento['a1']['dono'] = 'sra. lucia'

# Adicionando nova vaga
estacionamento['d4'] = {
    'marca': 'chevrolet',
    'modelo': 'onix',
    'dono': 'sr. roberto'
}

# Exibindo dados
print("Dono da vaga a1:", estacionamento['a1']['dono'])
print("Nova vaga d4:", estacionamento['d4'])
print("Marca na vaga a1:", estacionamento['a1']['marca'])