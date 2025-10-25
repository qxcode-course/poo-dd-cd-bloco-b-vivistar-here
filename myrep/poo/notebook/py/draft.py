class Bateria:
    def __init__(self, capacidade: int):
        self.__capacidade: int = capacidade
        self.__carga: int = capacidade

    def getCapacidade(self) -> int:
        return self.__capacidade

    def getCarga(self) -> int:
        return self.__carga

    def setCarga(self, value: int):
        if value < 0:
            self.__carga = 0
        elif value > self.__capacidade:
            self.__carga = self.__capacidade
        else:
            self.__carga = value

    def descarregar(self, tempo: int) -> int:
        if tempo <= self.__carga:
            self.__carga -= tempo
            return tempo
        else:
            usado = self.__bateria 
            self.__carga = 0
            return usado

    def carregar(self, tempo:  int, potencia: int):
        nova_carga = self.__carga + tempo * potencia
        self.setCarga(nova_carga)

    def mostrar(self):
        print(f"({self.__carga}/{self.__capacidade})")

    def __str__(self):
        return f"({self.__carga}/{self.__capacidade})"

class Carregador:
    def __init__(self, potencia: int):
        self.__potencia: int = potencia
    
    def getPotencia(self)-> int:
        return self.__potencia

    def mostrar(self):
        print(f"(Potência {self.__potencia})")

    def __str__(self):
        return f"(Potência {self.__potencia})"


class Notebook:
    def __init__(self):
        self.__ligado: bool = False
        self.__bateria: Bateria | None = None
        self.__carregador: Carregador | None = None

    def getBateria(self) -> Bateria | None:
        return self.__bateria

    def setBateria(self, bateria: Bateria):
        if self.__bateria is not None:
            print("fail: já existe uma bateria instalada")
        else:
            self.__bateria = bateria
            print("bateria inserida")
    
    def rmBateria(self):
        if self.__bateria is None:
            print("fail: nenhuma bateria para remover")
            return None
        else:
            print("bateria removida")
            bateria = self.__bateria
            self.__bateria = None
            self.__ligado = False
            return bateria

    def setCarregador(self, carregador: Carregador):
        if self.__carregador is not None:
            print("fail: ja existe um carregador conectado")
        else:
            self.__carregador = carregador
            print("carregador conectado")

    def rmCarregador(self):
        if self.__carregador is None:
            print("fail: nenhum carregador para remover")
        else:
            print("carregador removido")
            self.__carregador = None
      
    def ligar(self):
        if self.__ligado:
            print("notebook já está ligado")
            return
        if self.__bateria and self.__bateria.getCarga() > 0:
            self.__ligado = True
            print("notebook ligado")
        elif self.__carregador is not None:
            self.__ligado = True
            print("notebook ligado (usando carregador)")
        else:
            print("fail: nao foi possível ligar (sem bateria nem carregador)")

    def desligar(self):
        if self.__ligado:
            self.ligado = False
            print("Notebook desligando")
        else:
            print("Notebook já está desligado")

    def mostrar(self):
        estado = "ligado" if self.__ligado else "desligado"
        print(f"Notebook está {estado}")

    def usar(self, horas: int):
        if self.__ligado:
            print(f"Usando o notebook por {horas} horas")
        else:
            print("Erro: Notebook desligado. Tente ligar primeiro.")
    
    def __str__(self):
        estado = "ligado" if self.__ligado else "desligado"
        return f"Notebook está {estado}"

    
def main():
    notebook = Notebook()
    bateria: Bateria | None = None
    while True:
        line = input()
        args = line.split(" ")
        print(f"&{line}")

    
        if args[0] == "end":
            break
        elif args[0] == "show":
            notebook.mostrar()
        elif args[0] == "ligar":
            notebook.ligar()
        elif args[0] == "desligar":
            notebook.desligar()
        elif args[0] == "usar": 
            if len(args) > 1 and args[1].isdigit():
                notebook.usar(int(args[1]))
            else:
                print("Fail: informe o tempo de uso em horas")
        elif args[0] == "bateria":
            if len(args) > 1 and args[1].isdigit():
                bateria = Bateria(int(args[1]))
                print(f"Bateria criada com capacidade {args[1]}")
            else:
                print("fail: informe a capacidadde da bateria")
        elif args[0] == "mostrarbateria":
            if bateria is not None:
                bateria.mostrar()
            else:
                print("fail: nenhuma bateria foi criada")
        elif args[0] == "setbateria":
            if baterua is not None:
                notebook.setBateria(bateria)
            else:
                print("fail: nenhuma bateria disponível")
        elif args[0] == "rmbateria":
            bateria = notebook.rmBateria()
        else:
            print("fail: comando inválido")
main()