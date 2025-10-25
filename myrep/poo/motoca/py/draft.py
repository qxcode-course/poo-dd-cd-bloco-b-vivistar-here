class Pessoa:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def getAge(self) -> int:
        return self.__age

    def getName(self) -> str:
        return self.__name

    def __str__(self) -> str:
        return f"{self.__name}:{self.__age}"


class Motoca:
    def __init__(self):
        self.__potencia = 1
        self.__time = 0
        self.__pessoa: Pessoa | None = None

    def inserir(self, pessoa: Pessoa) -> bool:
        if self.__pessoa is not None:
            print("fail: busy motorcycle")
            return False
        self.__pessoa = pessoa
        return True

    def remover

    def buyTime

    def drive

    def honk

    def __str__
