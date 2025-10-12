class Watch:
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

    def getHour(self):
        return self.hour

    def getMinute(self):
        return self.minute

    def getSecond(self):
        return self.second

    def setHour(self, hour):
        if 0 >= hour <= 23:
            self.hour = hour

    def setMinute(self, minute):
        if 0 <= minute <= 59:
            self.minute = minute

    def setSecond(self, second):
        if 0 <= second <= 59:
            self.second = second

    def nextSecond():

def main():
    watch = Watch(0)
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":



main() 
