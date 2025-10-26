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
        if self.__motorista is not None:
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
            print(f"{self.__passageiro.getNome()} pagou R${pago:.2f}")
        self.__passageiro = None
        self.__custo = 0

    def __str__(self):
        if self.__motorista is not None:
            motorista = f"{self.__motorista.getNome()}:{int(self.__motorista.getDinheiro())}"
        else:
            motorista = "None"

        if self.__passageiro is not None:
            passageiro = f"{self.__passageiro.getNome()}:{int(self.__passageiro.getDinheiro())}"
        else:
            passageiro = "None"
        return f"Cost: {int(self.__custo)}, Driver: {motorista}, Passenger: {passageiro}"


def main():
    moto = Moto()
    pessoas ={}

    while True:
        line = input()
        args = line.split()
        print("$" + line)

        if args[0] == "end":
            break

        elif args[0] == "addPerson":
            nome = args[1]
            dinheiro = float(args[2])
            pessoas[nome] = Pessoa(nome, dinheiro)

        elif args[0] == "setDriver":
            nome = args[1]
            dinheiro = float(args[2])
            motorista = Pessoa(nome, dinheiro)
            moto.setMotorista(motorista)

        elif args[0] == "rmMotorista":
            moto.removerMotorista()

        elif args[0] == "subir":
            nome = args[1]
            if nome in pessoas:
                moto.subiuPassageiro(pessoas[nome])
            else:
                print("fail: pessoa nao encontrada")

        elif args[0] == "dirigir":
            km = float(args[1])
            moto.dirigir(km)

        elif args[0] == "descer":
            moto.descerPassageiro()

        elif args[0] == "show":
            if moto:
                print(moto)
            else:
                print("fail: moto nao inicializada")

        else:
            print("fail: comando invalido")
main()
