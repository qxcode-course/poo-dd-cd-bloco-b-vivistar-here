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

    def descarregr(self, tempo: int) -> int:
        if tempo <= self.__carga:
            self.__carga -= tempo
            return tempo
        else:
            usado = self.__carga 
            self.__carga = 0
            return usado

    def mostrar(self):
        print(f"({self.__carga}/{self.__capacidade})")

    def __str__(self):
        return f"({self.__carga}/{self.__capacidade})"


class Notebook:
    def __init__(self):
        self.__ligado: bool = False
      
    def ligar(self):
        if not self.__ligado:
            self.__ligado = True
            print("Notebook ligando")
        else:
            print("O notebook já está ligado")
        
    def desligar(self):
        if not self.__ligado:
            self.ligado = Falso
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

        if len(args) == 0:
            continue

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
        else:
            print("Fail: comando inválido")

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

        elif args[0] == "descarregar":
            bateria = notebook.descarregar()

        else:
            print("fail: comando inválido")
main()