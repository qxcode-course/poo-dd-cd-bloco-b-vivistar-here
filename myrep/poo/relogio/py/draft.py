class Watch:
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

    def getHour(self):

    def getMinute(self):

    def getSecond(self):

    def setHour():

    def setMinute():

    def setSecond():

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
