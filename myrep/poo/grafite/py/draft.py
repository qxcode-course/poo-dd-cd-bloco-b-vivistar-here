class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.__calibre = calibre
        self.__dureza = dureza
        self.__tamanho = tamanho

    def getCalibre(self) -> float:
        return self.__calibre

    def getDureza(self) -> str:
        return self.__dureza

    def getTamanho(self) -> int:
        return self.__tamanho

    def setTamanho(self, value: int):
        self.__tamanho = value

    def usagePerSheet(self) -> int:
        gasto = {"HB": 1, "2B": 2, "4B": 4, "6B": 6}
        return gasto.get(self.getDureza(), 0)

    def __str__(self):
        return f"{self.__calibre:.1f}:{self.__dureza}:{self.__tamanho}"

class Lapiseira:
    def __init__(self, calibre: float):
        self.__calibre = calibre
        self.__grafite: Grafite | None = None

    def hasGrafite(self) -> bool:
        return self.__grafite is not None
    
    def insert(self, grafite: Grafite):
        if self.hasGrafite():
            print("fail: ja existe grafite")
            return
        if grafite._Grafite__calibre != self.__calibre:
            print("fail: calibre incompativel")
            return
        self.__grafite = grafite

    def remove(self) -> Grafite | None:
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return None
        grafite = self.__grafite 
        self.__grafite = None
        return grafite

    def write(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return

        grafite = self.__grafite
        tamanho = grafite.getTamanho()
        gasto = grafite.usagePerSheet()

        if tamanho <= 10:
            print("fail: tamanho insuficiente")
            return 

        if tamanho - gasto < 10:
            grafite.setTamanho(10)
            print("fail: folha incompleta")
            return

        grafite.setTamanho(tamanho - gasto)


    def __str__(self):
        if self.__grafite:
            return f"calibre: {self.__calibre:.1f}, grafite: [{self.__grafite}]"
        else:
            return f"calibre: {self.__calibre:.1f}, grafite: null"

def main():
    lapiseira: Lapiseira | None = None
    grafite: Grafite | None = None

    while True:
        line = input()
        args = line.split()
        print("$" + line)

        if args[0] == "end":
            break

        elif args[0] == "init":
            lapiseira = Lapiseira(float(args[1]))

        elif args[0] == "insert":
            if lapiseira is None:
                print("fail: lapiseira não inicializada")
                continue
            grafite = Grafite (float(args[1]), args[2], int(args[3]))
            lapiseira.insert(grafite)

        elif args[0] == "remove":
            if lapiseira is None:
                print("fail: lapiseira não inicializada")
                continue
            grafite = lapiseira.remove()

        elif args[0] == "write":
            if lapiseira is None:
                print("fail: lapiseira não inicializada")
                continue
            lapiseira.write()

        elif args[0] == "show":
            if lapiseira:
                print(lapiseira)
            else:
                print("fail: lapiseira não inicializada")
        else:
            print("fail: comando inválido")

main()
