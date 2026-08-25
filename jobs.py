from main import Task

class Job(Task):
    pass

    def job(self, name, hourlyWage, bonus):
        self.name = name
        self.hourlyWage = hourlyWage
        self.bonus = bonus

    def printJob(self):
        return f'{self.name} {self.hourlyWage} {self.bonus} {self.stress}'
if __name__ == '__main__':
    job1 = Job('Business Analyst', 50, 75)
    print(job1.printJob)