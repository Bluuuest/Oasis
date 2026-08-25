from jobs import Job
from errands import Errand
from tasks import Task

'''
here, we are defining the new main function,
to manage the program's menu and logistics
managing the user's info
'''
'''
main function asks user for input on guest vs account
'''
def main():

    def taskSubmenu():
        print('=' * 75)
        print(f'     1. Add a new task')
        print(f'     2. Overwrite a task')
        print(f'     3. Delete a task')
        print(f'     4. Go back!')
        print('=' * 75)

    def jobSubmenu():
        print('=' * 75)
        print(f'     1. Create a new job')
        print(f'     2. Grant bonus')
        print(f'     3. Increase hourly wage')
        print(f'     4. Go back!')
        print('=' * 75)

    def errandSubmenu():
        print('=' * 75)
        print(f'     1. Mark as complete')
        print(f'     2. Collect Reward')
        print(f'     3. Create New Errand')
        print(f'     4. Go Back!')
        print('=' * 75)

    task1 = Task('Meal Prep', 5, 25)
    task2 = Task('Taxiing', 5, 50)
    task3 = Task('Package Shipping', 5, 25)
    task4 = Task('File Management', 10, 75)
    task5 = Task('DIY Project', 15, 125) 

    jobClass = Job

    job1 = jobClass('Accounting', 40, 50)
    job2 = jobClass('IT Project Director', 75, 100)
    job3 = jobClass('Aerial Cargo Pilot', 65, 75)
    job4 = jobClass('Agriculturalist', 50, 95)
    job5 = jobClass('Small Business Owner', 100, 200)

    errandClass = Errand

    errand1 = errandClass('Post Office Walk', 5, 15)
    errand2 = errandClass('Pass Go/Collect $200', 10, 20)
    errand3 = errandClass('Pen Pal Letter', 15, 30)
    errand4 = errandClass('Rx Pickup', 10, 20)
    errand5 = errandClass('Packaging', 20, 30)

    taskList = [task1, task2, task3, task4, task5]
    jobList = [job1, job2, job3, job4, job5]
    errandList = [errand1, errand2, errand3, errand4, errand5]
    completedErrands = []
    email = ' '
    newName = ' '
    newHours = 0
    newTask = ' '
    newJob = ' '
    chooseType = 0
    reattemptLogin = 'y'

    while reattemptLogin == 'y':
        answer1 = int(input('Login as Guest or create account?; (1 = Guest, 2 = Create) '))
        if answer1 == 1:
            email = 'Guest'
        elif answer1 == 2:
            email = str(input('Please type in your email;   '))
            password = str(input('Please type in a password;    '))
            age = int(input('Please type in your age, number only;  '))
        else:
            if not isinstance(answer1, int) or answer1 > 2:
                print('Invalid data given, please try again.')
                return

        print('                   [', '-' * 10, 'Task Manager', '-' * 10, ']')

        while True:
            print('=' * 75)
            print(f'Welcome, {email}')
            print('     1. Pull Up Tasks Recorded')
            print('     2. Track Productivity')
            print('     3. Job Book')
            print('     4. Available Errands')
            print('     5. Log Out')
            answer2 = int(input('Type a number.;     '))

            if answer2 == 1:
                print('Here are all of your current tasks.;')
                print(taskList)
                print('-' * 15, 'Maximum of 5 Tasks', '-' * 15)
                for entry, task in enumerate(taskList):
                        print(entry, task)
                print('What would you like to do?;')
                taskSubmenu()

                option1Answer = int(input('Please type a number.;   '))

                if option1Answer == 1:
                    newName = str(input("Type in the task's name.   "))
                    newHours = int(input('How many hours did you spent on this task today?  '))
                    newExp = float(newHours * 5)
                    newTask = Task(newName, newHours, newExp)
                    taskList.append(newTask)
                    print(f'Successfully appended the new "{newName}" task to your list.')
                    continue

                elif option1Answer == 2:
                    for entry, task in enumerate(taskList):
                        print(entry, task)
                    entry = int(input('Pick a task to overwrite. [Pick a number]  '))
                    newName = str(input("Type in the task's name.   "))
                    newHours = int(input('How many hours did you spent on this task today?  '))
                    newExp = float(newHours * 5)
                    newTask = Task(newName, newHours, newExp)
                    taskList[entry] = newTask
                    print(f'Successfully overwritten the new "{newName}" task in your list.')

                elif option1Answer == 3:
                    print('=' * 75)
                    for entry, task in enumerate(taskList):
                        print(entry, task)
                    selection = int(input('Which one would you like to purge? [Pick a number] '))
                    deleteAsk = str(input('DO YOU REALLY WANT TO DO THIS? It will be deleted forever! [y/n]     '))

                    if deleteAsk == 'y':
                        taskList.pop(selection)
                    elif deleteAsk == 'n':
                        continue
                    else:
                        print('Invalid data given, please try again.')
                elif option1Answer == 4:
                    continue
                elif option1Answer == 5:
                    for entry, task in enumerate(taskList):
                        print(entry, task)
            
            elif answer2 == 2:
                newName = str(input('What was the name of this task?    '))
                chooseType = int(input('What type of task was it? [task = 1, job = 2, errand = 3]   '))
                newHours = float(input('How many hours did you spent on this task today?    '))
                newExp = newHours * 5
                newTask = Task(newName, newHours, newExp)

                if chooseType == 1:
                    taskList.append(newTask)
                elif chooseType == 2:
                    jobList.append(jobClass(newTask, newHours, newExp))
                elif chooseType == 3:
                    errandList.append(errandClass(newTask, newHours, newExp))

                print(f'You have logged; "{newName}" with {newHours} in hours, gaining {newExp} exp in return.')
                continue
            elif answer2 == 3:
                print('=' * 75)
                print('Here are all available jobs.;')
                for entry, job in enumerate(jobList):
                        print(entry, job)
                print('What would you like to do?')
                jobSubmenu()
                option2Answer = int(input('Please type a number.;   '))

                if option2Answer == 1:
                    newName = str(input("Type in name of your job.   "))
                    newHours = int(input('How many hours do you spend working?  '))
                    newExp = float(newHours * 10)
                    newJob = jobClass(newName, newHours, newExp)
                    taskList.append(newTask)
                    print(f'Successfully appended the new "{newName}" job to your job list +{newExp} EXP.')
                    continue

            elif answer2 == 4:
                print('=' * 75)
                print('Here are all available errands.;')
                for entry, errand in enumerate(errandList):
                        print(entry, errand)
                print('Completed errands;')
                for entry, completed in enumerate(completedErrands):
                        print(entry, completed)
                print('What would you like to do?')
                errandSubmenu()

                option3Answer = int(input('Please type a number.;   '))

                if option3Answer == 1:
                    for entry, errand in enumerate(errandList):
                        print(entry, errand)
                    errandSelection = int(input('Pick an errand to mark complete. [Pick a number]     '))
                    completionAnswer = str(input('Do you want to mark this errand as complete? [y/n]'))
                    if completionAnswer == 'y':
                        completedErrands.append(errand)
                        errandList.pop(errandSelection)
                        

                        

            elif answer2 == 5:
                print(f'Goodbye, {email}!')
                break
            elif not isinstance(answer2, int) or answer2 > 5:
                print('Invalid data given, please try again.')
                return
        reattemptLogin = str(input('Wanna log back in? (y/n)     '))
        if reattemptLogin == 'y':
            continue
        elif reattemptLogin == 'n':
            break
        else:
            print('Invalid data given, try again.')
main()