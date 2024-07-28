def task():
    tasks = []
    print("                                                  -----|Welcome To Task Management App|-----\n                                                                    ")
    
    total_task = int(input("Boss enter how many task's you want to Preform today= "))
    for i in range (1 , total_task+1):
        task_name = input(f"Enter task {i}:-")
        tasks.append(task_name)
    print(f"\nBoss this are your today's tasks:-\n{tasks}")
    
    take = input("\nType 'YES' to perform any Operation:-\n")
    take = take.lower()
    if take == "yes":
        
        while True:
            Operation = int(input("Enter\n1.Add\n2.Update\n3.Delete\n4.View\n5.Exit\nEnter your choice Boss:-"))
            if Operation == 1:
                add_task = input("Enter the task you need to Add:- ")
                tasks.append(add_task)
                print(f"\n[__Task {add_task} is Added Successfully__]\n")
                
            elif Operation == 2:
                update_task = input("Enter the task you want to Update:- ")
                if update_task in tasks:
                    new_task = input("Enter the New task:- ")
                    ind = tasks.index(update_task)
                    tasks[ind] = new_task
                    print(f"\n[__Task {new_task} is Updated__]\n")
                else:
                    print(f"\nEntered task '{update_task}' is not present in the List\n")
            elif Operation == 3:
                delete_task = input("Enter the task you want to Delete:- ")
                if delete_task in tasks:
                    ind = tasks.index(delete_task)
                    del tasks[ind]
                    print(f"\n[__Task {delete_task} is Deleated__]\n")
                else:
                    print(f"\nEntered task '{delete_task}' is not present in the List\n")
                    
            elif Operation == 4:
                print(f"\n[__Total tasks are__]\n\n{tasks}\n")
            
            elif Operation == 5:
                print("\nTHANK YOU\n")
                print("Closing the program......\n")
                break
            else:
                print("\nYou have entered invalid Choice\n")
                    
task()    
   
        


    