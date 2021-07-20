class ContaCorrente:

    def __init__(self, numero, titular, banco_numero, banco_nome, saldo, limite, cpf):
        self._numero = numero
        self.__titular__ = titular
        self.saldo = saldo
        self.limite = limite
        self.banco_nome = banco_nome
        self.banco_numero = banco_numero
        self._cpf = cpf

    def extrato(self):
        return f'Saldo de R$ {self.saldo} do titular {self.__titular__}'

    def depositar(self, valor):
        self.saldo += valor

    def __saque_autorizado__(self, valor_a_sacar):
        valor_disp_saque = self.saldo + self.limite
        return valor_a_sacar <= valor_disp_saque

    def sacar(self, valor=0):
        if self.__saque_autorizado__(valor):
            self.saldo -= valor
        else:
            print(f'O valor R$ {valor} ultrapassou seu limite. SAQUE NEGADO')

    def dados_conta(self):
        return print((self._numero, self.__titular__, self.banco_numero,
                      self.banco_nome, self.saldo, self.limite, self._cpf))

    def transferir(self, valor, destino):
        if self.__saque_autorizado__(valor):
            self.sacar(valor)
            destino.depositar(valor)
        else:
            return f'Transferência no valor de R${valor:.2f}, NEGADA!'
    
    def limite(self, limite):
        self.limite = limite


class Cliente:

    def __init__(self, nome):
        self.__nome__ = nome

    @property
    def nome(self):
        return self.__nome__.title()

    @nome.setter
    def nome(self, nome):
        self.__nome__ = nome