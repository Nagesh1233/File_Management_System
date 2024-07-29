student_grade = {}

def add_student(name, grade):
    if name in student_grade:
        print(f"\nThe Student='{name}' already exists. Please use a unique name.")
    else:
        student_grade[name] = grade
        print(f"\nThe Student='{name}' with Grade= {grade} is added")

    
def update_student(name):
    if name in student_grade:
        try:
            grade = int(input(f"Enter the updated Grade of Student '{name}'= "))
            student_grade[name] = grade
            print(f"\nThe Student='{name}' Updated with Grade= {grade}\n")
        except ValueError:
            print("Enter the valid Grade number")
    else:
        print(f"\nThe Student Name '{name}' is not predent in List\n")
        
def delete_student(name):
    del student_grade[name]
    print(f"\nThe Student '{name}' is Deleated\n")
    
        
def desplay_student():
    if student_grade:
        print(f"\n{len(student_grade)} Students are present in List")
        for name , grade in student_grade.items():
            print(f"\n{name} : {grade}")
            
    else:
        print("\nNo students found\n")
        
#-----------------------------------------------------------------------------------------------------------------------------------------------
            
def main():
    
    print("\n  ----Welcome to Student Grade Management System----\n")
    while True:
        print("         |------------------------------|")
        print("         |___|This are your Options.|___|")
        print("         |------------------------------|")
        print("         |Press 1. to Add Student       |")
        print("         |Press 2. to Update student    |")
        print("         |Press 3. to Delete Student    |")
        print("         |Press 4. to View Students     |")
        print("         |Press 5. to Exit              |")
        print("         |------------------------------|")
        
        try:
            options = int(input("\nEnter your choice hear = "))
        except ValueError:
            print("\nPut correct Option\n")
            continue
        
#-----------------------------------------------------------------------------------------------------------------------------------------------        
        
        if options == 1:
            while True:
                try:
                    times = int(input("How many Student's do you want to Add = "))
                    break
                except ValueError:
                    print("Enter valid Input")
                    
            successfully_added = 0        
            for i in range(times):
                while True:
                    name = input(f"\nEnter the Student name {i+1} = ")
                    if name.isdigit():       #It will check weather the input in valid or not if it is in digit it will display the bellow print satement
                        print("Enter valid Name")
                    elif name in student_grade:
                        print(f"\nThe Student='{name}' already exists. Please use a unique name.")
                    else:
                        break
                        
                while True:
                    try: #this is used to check the input is correct or not if input is not in integer it will display error statement
                        grade = int(input("Enter the Grade = "))
                        break
                    except ValueError:
                        print("Enter valid Grade number")
                add_student(name,grade)
                successfully_added += 1  # Increment the counter for each successful addition
    
            print(f"\n{successfully_added} Students were successfully added.\n")
            input("\nPress Enter to continue...\n")
            print("Continue if you want to perform any Operation\n")
            
#-----------------------------------------------------------------------------------------------------------------------------------------------------
                        
        elif options == 2:
            
            while True:
                try:
                    times = int(input("How many Student's Grade do you want to Update = "))
                    if times > len(student_grade):
                        print(f"\nYou only have {len(student_grade)} students. Please enter a valid number.\n")
                    else:
                        break
                except ValueError:
                    print("Enter valid Input")
            
            Update_count = 0
            while Update_count < times:
                name = input(f"\nEnter the Student name {Update_count+1} = ")
                if name.isdigit():
                    print("Enter valid Name")
                elif name not in student_grade:
                    print(f"\nThe Student Name '{name}' is not present in List")
                else:
                    update_student(name)
                    Update_count += 1
            input("\nPress Enter to continue...\n")
            print("Continue if you want to perform any Operation\n")
                
            #This is the part of delete 
            
            
#----------------------------------------------------------------------------------------------------------------------------------------------------
            
        elif options == 3:
            while True:
                try:
                    times = int(input("How many Student's do you want to Delete = "))
                    if times > len(student_grade):
                        print(f"\nYou only have {len(student_grade)} students. Please enter a valid number.\n")
                    else:
                        break
                except ValueError:
                    print("Enter valid Input")
                    
            Deleate_count = 0
            while Deleate_count < times:
                name = input(f"\nEnter the Student name {Deleate_count+1} = ")
                if name.isdigit():
                    print("Enter valid Name")
                elif name not in student_grade:
                    print(f"\nThe Student Name '{name}' is not present in List")
                else:
                    delete_student(name)
                    Deleate_count += 1    
            input("\nPress Enter to continue...\n")
            print("Continue if you want to perform any Operation\n")    
          
#-----------------------------------------------------------------------------------------------------------------------------------------------
                    
        elif options == 4:
            desplay_student()
            input("\nPress Enter to continue...\n")
            print("Continue if you want to perform any Operation\n")
#-------------------------------------------------------------------------------------------------------------------------------------------------           
            
        elif options == 5:
            print("\nClosing......")
            break
            
#-------------------------------------------------------------------------------------------------------------------------------------------------            
            
        else:
            print("\nPut correct Option\n")
            
main()
            
            
            
            