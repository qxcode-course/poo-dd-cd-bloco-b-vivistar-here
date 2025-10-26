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
        