task = input('Enter a the task: ')
priority = input('Enter the tasks priority (high,medium,low): ')
time_bound = input('Is the task time bound? (yes/no): ')

match priority:
    
        
    case 'high':
        print(f'{task} ias a high priority task. Consider completing it soon!!')

        if time_bound == 'yes':
            print(f'{task} is a high priority task with a dealine, please remember the deadline and complete it soon')


    case 'medium':
        print(f'{task} ias a medium priority task. Consider completing it when you can!!')

        if time_bound == 'yes':
            print(f'{task} is a medium priority task with a dealine, please remember the deadline and complete it')


    case 'low':
        print(f'{task} ias a low priority task. Consider completing it when you are free!!')

        if time_bound == 'yes':
            print(f'{task} is a low priority task with a dealine, please remember the deadline and complete it when you have free time')

    
