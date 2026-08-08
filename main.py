class Oasis:
    def __init__(self, name, time_hours, exp):
        self.name = name
        self.time_hours = time_hours
        self.exp = exp

    '''
    this should print an error if amount of hours
    and exp is below 0
    '''
    def error(self, checker):
        if self.time_hours < 0 or self.exp < 0:
            print('Error; Value cannot be negative')
        elif self.time_hours > 100 or self.exp > 100:
            time_hours += 25
            exp += 25
        else:


if __name__ == '__main__':
    task1 = Oasis('Money Laundering', 730, -28)