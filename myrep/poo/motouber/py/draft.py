class Pessoa:
    def __init__(self, nome: str, dinheiro: float):
        self.__nome = nome
        self.__dinheiro = dinheiro

    def getNome(self) -> str:
        return self.__nome

    def getDinheiro(self) -> float:
        return self.__dinheiro

    def pagar(self, value: float):
        if value > self.__dinheiro:
            valor_pago = self.__dinheiro
            self.__dinheiro = 0
            return valor_pago
        else:
            self.__dinheiro -= value
            return value

    def receber(self, value: float):
        self.__dinheiro += value

    def __str__(self):
        return f"{self.__nome}: R$ {self.__dinheiro:.2f}"



class Moto:
    def __init__(self):
        self.__motorista = None
        self.__passageiro = None
        self.__custo = 0

    def setMotorista(self, motorista: Pessoa):
        if motorista is not None:
            print("fail: ja existe motorista")
            return
        self.__motorista = motorista

    def removerMotorista(self):
        if self.__motorista is None:
            print("fail: nao existe motorista")
            return
        self.__motorista = None

    def subiuPassageiro(self, passageiro: Pessoa):
        if self.__motorista is None:
            print("fail: nao existe motorista")
            return
        if self.__passageiro is not None:
            print("fail: ja existe passageiro na moto")
            return
        self.__passageiro = passageiro
        self.__custo = 0
        print(f"passageiro {passageiro.getNome()} subiu na moto")

    def dirigir(self, km: float):
        if self.__passageiro is None:
            print("fail: nao existe passageiro na moto")
            return
        self.__custo += km

    def descerPassageiro(self):
        if self.__passageiro is None:
            print("fail: nao ha passageiro pra descer")
            return
        print(f"{self.__passageiro.getNome()} desceu. Corrida custou R${self.__custo:.2f}")
        pago = self.__passageiro.pagar(self.__custo)
        self.__motorista.receber(self.__custo)
        if pago < self.__custo:
            print(f"{self.__passageiro.getNome()} pagou R${pago:.2f}, Uber completou o resto do valor")
        else:
            print(f"{self._passageiro.getNome()} pagou R${pago:.2f}")
        self.__passageiro = None
        self.__custo = 0

    def __str__(self):
        motorista = self.__motorista.getNome() if self.__motorista is not None else "nenhum"
        passageiro = self.__passageiro.getNome() if self.__passageiro else "nenhum"
        print(f"Motorista: {motorista}, Passageiro: {passageiro}, Custo: R${self.__custo:.2f}")


