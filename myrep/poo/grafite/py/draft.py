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
        return gasto.get(getDureza(), 0)

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
            print("Já existe grafite na lapiseira")
            return
        if grafite._Grafite__calibre != self.__calibre:
            print("Calibre incompatível")
            return
            self.__grafite = grafite

    def remove(self) -> Grafite | None:
        if not self.hasGrafite():
            print("fail: não existe grafite na lapiseira")
            return None
        grafite = self.__grafite 
        self.__grafite = None
        return grafite

    def write(self):
        if not self.hasGrafite():
            print("fail: não existe grafite na lapiseira")
            return
        if tamanho <= 10:
            print("fail: tamanho insuficiente de grafite")
            return 
        if tamanho - gasto < 10:
            grafite.setTamanho(10)
            print("fail: folha incompleta")
            return

        grafite.setTamanho(tamanho - gasto)


    def __str__(self):
        if self.__grafite:
            return f"calibre:{self.__calibre:.1f}, grafite:{self.__grafite}"
        else:
            return f"calibre:{self.__calibre:.1f}, grafite:(null)"

def main():

main()
