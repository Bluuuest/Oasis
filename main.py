'''
here, we are defining the new main function,
to manage the program's menu and logistics
managing the user's info
'''
'''
main function asks user for input on guest vs account
'''
def main():

    taskList = []
    jobList = []
    errandList = []
    email = ' '
    newName = ' '
    newHours = 0
    newTask = ' '
    chooseType = 0

    answer1 = int(input('Login as Guest or create account?; (1 = Guest, 2 = Create) '))
    if answer1 == 1:
        email = 'Guest'
    elif answer1 == 2:
        email = str(input('Please type in your email;   '))
        password = str(input('Please type in a password;    '))
        age = int(input('Please type in your age, number only;  '))
    else:
        print('Invalid data given, please try again.')
        return

    print('                   [', '-' * 10, 'Task Manager', '-' * 10, ']')

    while True:
        print('=' * 75)
        print(f'Welcome, {email}')
        print('     1. Pull Up Tasks Recorded')
        print('     2. Track Productivity')
        print('     3. Job Book')
        answer2 = int(input('Type a number.;     '))

        if answer2 == 1:
            print('Here are all of your current tasks.;')
            print(taskList)
            print('-' * 15, 'Maximum of 5 Tasks', '-' * 15)
            print('What would you like to do?;')
            print('     1. Add a new task')
            print('     2. Overwrite a task')
            print('     3. Delete a task')
            print('     4. Go back!')
            print('     5. Examine a task')

            option1Answer = int(input('Please type a number.;   '))

            if option1Answer == 1:
                newName = str(input("Type in the task's name.   "))
                newHours = int(input('How many hours did you spent on this task today?  '))
                newExp = float(newHours * 5)
                newTask = Task(newName, newHours, newExp)
                taskList.append(newTask)
                print(f'Successfully appended the new "{newName}" task to your list.')
                continue
        
        elif answer2 == 2:
            newName = str(input('What was the name of this task?    '))
            chooseType = int(input('What type of task was it? [task = 1, job = 2, errand = 3]   '))
            newHours = float(input('How many hours did you spent on this task today?    '))
            newExp = newHours * 5
            newTask = Task(newName, newHours, newExp)

            if chooseType == 1:
                taskList.append(newTask)
            elif chooseType == 2:
                jobList.append(newTask)
            elif chooseType == 3:
                errandList.append(newTask)

            print(f'You have logged; "{newName}" with {newHours} in hours, gaining {newExp} exp in return.')
            continue
        elif answer2 == 3:
            print('Here are all available jobs.;')
        elif not isinstance(answer2, int) or answer2 > 5:
            print('Invalid data given, please try again.')

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