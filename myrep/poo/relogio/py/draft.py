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
        if 0 <= hour <= 23:
            self.hour = hour

    def setMinute(self, minute):
        if 0 <= minute <= 59:
            self.minute = minute

    def setSecond(self, second):
        if 0 <= second <= 59:
            self.second = second

    def nextSecond(self):
        self.second += 1
    if self.second > 59:
        self.second = 0
        self.minute += 1
        if self.minute > 59:
            self.minute = 0
            self.hour += 1
            if self.hour > 23:
                self.hour = 0
                
    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"


def main():
    watch = Watch()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "init":
            h = int(args[1])
            m = int(args[2])
            s = int(args[3])
            watch.setHour(h)
            watch.setMinute(m)
            watch.setSecond(s)
        
        elif args[0] == "set":
            if args[1] == "hour":
                 watch.setHour(int(args[2]))
            elif args[1] == "minute":
                watch.setMinute(int(args[2]))
            elif args[1] == "second":
                watch.setSecond(int(args[2]))

        elif args[0] == "show":
            print(watch)

        elif args[0] == "next":
            watch.nextSecond()

        else:
            print("fail: comando invalido")
        
main() 
