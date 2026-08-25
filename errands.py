from tasks import Task

class Errand(Task):
    pass

    def Errand(self, name, incentive, energySpent, commuteType):
        super().__init__(name)
        self.name = name
        self.incentive = incentive
        self.energySpent = energySpent
        self.commuteType = commuteType

    def printErrand(self):
        return f'{self.name} {self.incentive} {self.energySpent} {self.commuteType}'

if __name__ == '__main__':
    errand1 = Errand(Task('a', 25, 50))
    print(errand1)