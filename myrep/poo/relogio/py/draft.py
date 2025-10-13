class Watch:
    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0

        self.setHour(hour)kkkkkk
        self.setMinute(minute)
        self.setSecond(second)

    def __str__(self) -> str:
        hour = self.getHour()
        minute = self.getMinute()
        second = self.getSecond()
        return f"{hour:02}:{minute:02}:{second:02}"

    def getHour(self) -> int:
        return self.__hour

    def getMinute(self) -> int:
        return self.__minute

    def getSecond(self) -> int:
        return self.__second

    def setHour(self, value: int):
        if value < 0 or value > 23:
            print("fail: hora invalida")
            return

        self.__hour = value

    def setMinute(self, value: int):
        if value < 0 or value > 59:
            print("fail: minuto invalido")
            return

        self.__minute = value

    def setSecond(self, value: int):
        if value < 0 or value > 59:
            print("fail: segundo invalido")
            return

        self.__second = value

    def nextSecond(self):
        if self.getSecond() != 59:
            self.setSecond(self.getSecond() + 1)
        
        else:
            self.setSecond(0)
            if self.getMinute() != 59:
                self.setMinute(self.getMinute() + 1)
            
            else:
                self.setMinute(0)
                if self.getHour() != 23:
                    self.setHour(self.getHour() + 1)
                else:
                    self.setHour(0)
                    self.setMinute(0)
                    self.setSecond(0)

        return


def main():
    watch = Watch()
    while True:
        line = input()
        args = line.split(" ")
        print(f"${line}")
        
        match args[0]:
            case "show":
                print(watch)
            
            case "init":
                watch = Watch(int(args[1]), int(args[2]), int(args[3]))
            
            case "set":
                watch.setHour(int(args[1]))
                watch.setMinute(int(args[2]))
                watch.setSecond(int(args[3]))

            case "next":
                watch.nextSecond()

            case "end":
                break
            
            case _:
                print("fail: comando invalido")

main()
