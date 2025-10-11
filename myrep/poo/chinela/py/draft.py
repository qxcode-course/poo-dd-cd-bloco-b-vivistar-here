class Chinela:
    def __init__(self):
        self.__tamanho = 0

    def getTamanho(self):
        return self.__tamanho

    def setTamanho(self, value: int):
        if value < 20 or > 50:
            print("fail: O tamanho deve estar entre 20 e 50")
        elif value % 2 != 0:
            print("fail: O tamanho deve ser um número par")
        else:
            self.__tamanho = value

chinela = Chinela() 

while chinela.getTamanho() == 0: 
    print("Digite seu tamanho de chinela")
    tamanho = int(input()) 
    chinela.setTamanho(tamanho)

print("Parabens, você comprou uma chinela tamanho", chinela.getTamanho())