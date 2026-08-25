from main import Task

class Errand(Task):
    pass

    def Errand(self, incentive, energySpent, commuteType):
        self.incentive = incentive
        self.energySpent = energySpent
        self.commuteType = commuteType

    def printErrand(self):
        return f'{self.name} {self.incentive} {self.energySpent} {self.commuteType}'

if __name__ == '__main__':
    errand1 = Errand(Task('a', 25, 50))
    print(errand1)