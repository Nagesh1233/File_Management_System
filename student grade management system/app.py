student_grade = { } #empty dictionary

def add_student(name,grade):
    student_grade[name] = grade
    
    print(f"Added {name} with {grade}")
    
    
def update_student(name,grade):
    if name in student_grade:
        student_grade[name] = grade
        
        print(f"{name} with marks are updated {grade}")
    
    else:
        print(f"{name} is not found!")
        
def deleat_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"{name} has been successfully deleted")
        
    else:
        print(f"{name} is not found!")

def desplay_all_students():
    if student_grade:
        for name, grade in student_grade.items():
            print(f"{name} : {grade}")
            

    else:
        print("No student found")
        
        
def main():
    while True:
        print("\n Student Grade Management System")
        print("1. Add Student")
        print("2. Add Update Student")
        print("3. Add Deleat Student")
        print("4. Add View Student")
        print("5. Exit")
    
        choice = int(input("Enter your choice = "))
        
        if choice == 1:
            name = input("Enter student name = ")
            grade = int(input("Enter the student grade = "))
            add_student(name , grade)
            
        elif choice == 2:
            name = input("Enter the student name = ")
            grade = int(input("Enter student grade = "))
            update_student(name,grade)
            
        elif choice == 3:
            name = input("Enter the student name = ")
            deleat_student(name)
            
        elif choice == 4:
            desplay_all_students()
            
        elif choice == 5:
            print("Closing........")
            break
        
        else:
            print("Invalid option")
        
    
main()
        
