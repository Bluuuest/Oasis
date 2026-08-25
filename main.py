'''
here, we are defining the new main function,
to manage the program's menu and logistics
managing the user's info
'''

'''
asks user for input on guest vs account
'''
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

    newName = ' '
    newHours = 0

    if answer1 == 1 or answer1 == 2:
        print(f'Welcome, {email}')
        print('     1. Pull Up Tasks Recorded')
        print('     2. Track Productivity')
        print('     3. Log Out')

    answer2 = int(input('Type a number.;     '))

    if answer2 == 1:
        print(Task.printTasks)
    elif answer2 == 2:
        newName = str(input('What was the name of this task?    '))
        newHours = float(input('How many hours did you spent on this task today? #    '))
        newExp = newHours * 5
        newTask = Task(newName, newHours, newExp)
        print(f'You have logged; "{newName}" with {newHours} in hours, gaining {newExp} exp in return.')
        print(newTask)
    elif answer2 == 3:
        print('Goodbye!')
        return

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

    def printTasks(self):
        print(Task())

if __name__ == '__main__':
    task1 = Task('Money Laundering', 730, -28)
    task2 = Task('Backflip', 0.1, 50)
    task3 = Task('Apple Picking', 2, 25)
    task4 = Task('Package Shipping', 0.5, 25)
    taskList = [task1, task2, task3, task4]

    main()