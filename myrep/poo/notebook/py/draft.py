class Notebook:
    def __init__(self):
        self.__ligado: bool = False
        self.mostrar(mostrar)
        self.usar(usar)
        self.ligar(ligar)

    def ligar(self):
        if self.__ligado:
            self.__ligado = True
            print("Notebook ligando")
        else:
            print("O notebook já está ligado")
        
    def desligar(self):
        if self.__ligado:
            self.ligado = Falso
            print("Notebook desligando")
        else:
            print("Notebook já está desligado")
        
        notebook = Notebook()
notebook.mostrar()
notebook.usar(10)
notebook.ligar()
notebook.mostrar()
notebook.usar(10)
notebook.desligar()

def main():
    notebook = Notebook()
    while True:
        line = input()
        args = line.split(" ")
        print(f"&{line}")

    match args[0] == "mostrar":
    print(Notebook)

main()