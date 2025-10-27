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
        return f"{self.__nome}:R${self.__dinheiro:.2f}"



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

    def dirigir(self, km: float):
        if self.__passageiro is None:
            print("fail: nao existe passageiro na moto")
            return
        self.__custo += km

    def descerPassageiro(self):
        if self.__passageiro is None:
            print("fail: nao existe passageiro na moto")
            return
        if self.__passageiro.getDinheiro() < self.__custo:
            print("fail: Passenger does not have enough money")
        else:
            pago = self.__passageiro.pagar(self.__custo)
            self.__motorista.receber(pago)
            print(f"{self.__passageiro.getNome()}:{int(self.__passageiro.getDinheiro())} left")
            
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
            if nome not in pessoas:
                pessoas[nome] = Pessoa(nome, dinheiro)
            moto.setMotorista(pessoas[nome])

        elif args[0] == "rmMotorista":
            moto.removerMotorista()

        elif args[0] == "setPass":
            nome = args[1]
            dinheiro = float(args[2])
            if nome not in pessoas:
                pessoas[nome] = Pessoa(nome, dinheiro)
            moto.subiuPassageiro(pessoas[nome])

        elif args[0] == "drive":
            km = float(args[1])
            moto.dirigir(km)

        elif args[0] == "leavePass":
            moto.descerPassageiro()

        elif args[0] == "show":
            if moto:
                print(moto)
            else:
                print("fail: moto nao inicializada")

        else:
            print("fail: comando invalido")
main()
