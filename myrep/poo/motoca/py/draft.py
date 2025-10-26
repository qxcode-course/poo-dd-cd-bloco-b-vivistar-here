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
    def __init__(self, power: int = 1):
        self.__power = power
        self.__time = 0
        self.__pessoa: Pessoa | None = None

    def inserir(self, pessoa: Pessoa) -> bool:
        if self.__pessoa is not None:
            print("fail: busy motorcycle")
            return False
        self.__pessoa = pessoa
        return True

    def remover(self) -> Pessoa | None:
        if self.__pessoa is None:
            print("fail: empty motorcycle")
            return None
        pessoa = self.__pessoa
        self.__pessoa = None
        return pessoa

    def buyTime(self, time: int):
        self.__time += time

    def drive(self, time: int):
        if self.__time <= 0:
            print("fail: buy time first")
            return
        if self.__pessoa is None:
            print("fail: empty motorcycle")
            return
        if self.__pessoa.getAge() > 10:
            print("fail: too old to drive")
            return
        if time > self.__time:
            print(f"fail: time finished after {self.__time} minutes")
            self.__time = 0
        else:
            self.__time -= time

    def honk(self):
        print("P" + "e" * self.__power + "m")

    def __str__(self):
        pessoa_str = "empty" if self.__pessoa is None else str(self.__pessoa)
        return f"power:{self.__power}, time:{self.__time}, person:({pessoa_str})"

def main():
    moto = Motoca()
    pessoa: Pessoa | None = None

    while True:
        line = input()
        args = line.split()
        print("$"+ line)

        if args[0] == "end":
            break

        elif args[0] == "init":
            if len(args) == 2 and args[1].isdigit():
                moto = Motoca(int(args[1]))
            else:
                moto = Motoca()

        elif args[0] == "show":
            print(moto)

        elif args[0] == "enter":
            if len(args) == 3:
                pessoa = Pessoa(args[1], int(args[2]))
                moto.inserir(pessoa)
            else:
                print("fail: informe nome e idade")
        
        elif args[0] == "leave":
            pessoa = moto.remover()
            if pessoa:
                print(f"{pessoa}")

        elif args[0] == "buy":
            if len(args) == 2 and args[1].isdigit():
                moto.buyTime(int(args[1]))
            else:
                print("fail: informe tempo em minutos")
        
        elif args[0] == "drive":
            if len(args) == 2 and args[1].isdigit():
                moto.drive(int(args[1]))
            else:
                print("fail: informe o tempo de direção")

        elif args[0] == "honk":
            moto.honk()

        else:
            print("fail: comando invalido")      

main()
