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
    while True:
        line = input()
        args = line.split(" ")
        print(f"&{line}")

    match args[0] == "mostrar":
    print(Notebook)

main()