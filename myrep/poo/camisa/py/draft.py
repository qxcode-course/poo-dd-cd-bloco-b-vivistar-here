class Camisa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self) -> str:
        return self.__tamanho
    
    def setTamanho(self, value: str):
        tamanhos_validos = ["PP", "P", "M", "G", "GG", "XG"]
        if value in tamanhos_validos:
            self.__tamanho = value
        else:
            print("fail: os tamanhos disponiveis sao PP, P, M, G, GG, XG")

def main():
        roupa = Camisa()
        while roupa.getTamanho() == "":
            print("Digite seu tamanho de roupa")
            tamanho = input()
            roupa.setTamanho(tamanho)
        print("Parabens, voce comprou uma roupa tamanho", roupa.getTamanho())

main()