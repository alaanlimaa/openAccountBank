import cadastro_cc.ccbanks as acao
from conta import ContaCorrente
import mysql.connector

connect = mysql.connector.connect(host='localhost', database='banks', user='root', password='28101565')
if connect.is_connected():
    print(f'\033[1;32mConectado ao servidor MySQL versão {connect.get_server_info()}\033[m')
cursor = connect.cursor()

while True:
    numero = str(acao.gerar_numero_conta()[:10])
    nome = str(acao.nome_titular()[:20])
    banco = acao.escolha_banco()
    saldo = float(acao.saldo_inical())
    limite = float(acao.limite_liberado(saldo))
    cpf = str(acao.numero_cpf()[:11])
    conta = ContaCorrente(numero, nome, int(banco[0]), str(banco[1][:20]), saldo, limite, cpf)
    conta.dados_conta()
    cursor.execute(f'insert into contas_bancarias values ("{conta._numero}", "{conta.__titular__}", '
                   f'{conta.banco_numero}, "{conta.banco_nome}", {conta.saldo}, {conta.limite}, '
                   f'"{conta._cpf}", now())')
    connect.commit()
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar criar outra conta [S/N]: ').strip().upper()[0]
    if resp == 'N':
        break

connect.close()
if connect.is_closed():
    print(f'\033[1;32mDados adcionados com sucesso no banco de dados MySQL versão {connect.get_server_info()}!\033[m')

