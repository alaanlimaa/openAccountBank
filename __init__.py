def gerar_numero_conta():
    from random import randint
    contanum = []
    for i in range(1, 10):
        if i == 8:
            contanum.append('-')
        else:
            n = randint(0, 9)
            contanum.append(n)
    numero = ''.join(map(str, contanum))
    return numero


def escolha_banco():
    import pandas as pd
    line()
    print(f'{"LISTA DE BANCOS".center(40)}')
    line()
    bancos = pd.read_csv('./numeros_bancos.csv', sep=';')
    print(pd.DataFrame(bancos))
    line()
    numbank = int(input('Digite o número banco desejado: '))
    for c in range(0, len(bancos)):
        if numbank == bancos['Numero'][c]:
            return numbank, f'{bancos["Banco Nome"][c]}'
    bancos.close()


def line():
    return print('=' * 40)

def nome_titular():
    nome = input('Qual nome do titular: ').title().strip()
    return nome

def saldo_inical():
    opcoes = {1: 250.00, 2: 500.00, 3: 750.00, 4: 1000.00, 5: 1500.00, 6: 3000.00}
    num = int(input('Tranferência inicial\n'
          '[1] R$ 250,00\n'
          '[2] R$ 500,00\n'
          '[3] R$ 750,00\n'
          '[4] R$ 1000,00\n'
          '[5] R$ 1500,00\n'
          '[6] R$ 3000,00\n'
        'Escolha uma opção acima: '))
    for k, v in opcoes.items():
        if k == num:
            return v


def limite_liberado(saldo_conta):
    if saldo_conta <= 750.00:
        return 1500.00
    elif saldo_conta <= 1500.00:
        return 2500.00
    else:
        return 4000.00


def numero_cpf():
    return input('Qual número CPF [APENAS NÚMEROS]: ')



