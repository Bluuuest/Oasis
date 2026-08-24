def main():
    email = 'empty'
    answer1 = int(input('Login as Guest or create account?; (1 = Guest, 2 = Create) '))
    if answer1 == 1:
        email = 'Guest'
    elif answer1 == 2:
        email = str(input('Please type in your email;   '))
        password = str(input('Please type in a password;    '))
        age = int(input('Please type in your age, number only;  '))

    print('[', '-' * 10, 'Task Manager', '-' * 10, ']')

    while True:
        print(f'Welcome, {email}')
        print('     1. Pull Up Tasks Recorded')
        print('     2. Track Productivity')
        print('     3. Log Out')
        if email == True:
            print('     4. Premium Membership')
        answer2 = input('Type a number.;     ')

class Task:
    def __init__(self, name, time_hours, exp):
        self.name = name
        self.time_hours = time_hours
        self.exp = exp
        self.error()

    '''
    this should print an error if amount of hours
    and exp is below 0
    '''
    def error(self):
        if self.time_hours <= 0 or self.exp <= 0:
            print('Error; Value cannot be negative')

if __name__ == '__main__':
    task1 = Task('Money Laundering', 730, -28)
    task2 = Task('Backflip', 0.1, 50)
    task3 = Task('Apple Picking', 2, 25)

    main()