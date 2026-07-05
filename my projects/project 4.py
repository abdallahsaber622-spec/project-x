tasks = []

while True:
    print ("____________________________")
    print("Welcome to the to-do list App")
    print("Choose an option:")
    print("1. Add new task")
    print("2. See my tasks")
    print("3. Delete task")
    print("4. Exit")
    print ("_____________________________")
    user_choice = int(input("Enter your choice (1,2,3,4): "))

    if user_choice == 1:
        task = input("Enter your task: ")
        tasks.append(task)
        print ("your task added ")
    elif user_choice == 2:
        if tasks == 0 :
            print ("you dont have task Enter number 1 to add tasks")
        else :
            print("Your Tasks:")
            print(f"You have {len(tasks)} tasks.")
            for task in tasks :
                print (task)
    elif user_choice == 3:
        print (tasks)
        for task in tasks :
            tasks_to_remove =input ("enter task to remove pls enter 1 task : ")
            if tasks_to_remove in tasks :
                tasks.remove(tasks_to_remove)
                print ("your task was removed")
            else :
                print ("this task is not added ")
    elif user_choice == 4:
        print ("okay goodbye  ")
        break   







     





           