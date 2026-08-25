class Task:
    def __init__(self, name, hoursSpent, exp):
        self.name = name
        self.hoursSpent = hoursSpent
        self.exp = exp
        self.error()

    '''
    this should print an error if amount of hours
    and exp is below 0
    '''
    def error(self):
        if self.hoursSpent <= 0 or self.exp <= 0:
            print('Error; Value cannot be negative')
    
    def __repr__(self):
        printable = self.__class__.__name__
        return f'{printable} (Name; {self.name}, Hours; {self.hoursSpent}), XP; {self.exp}'

if __name__ == '__main__':
    main()