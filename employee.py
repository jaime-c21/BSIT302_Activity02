class Employee:
 def __init__(self,name,department,position,rate):
        self.name = name
        self.department = department
        self.position = position
        self.rate = rate
     
    
start = True

employees = []



while start:
    print("""
        ******************************
        [1] Add new Employee
        [2] Enter hourly of Employee
        [3] Show Employee Information
        [4] Exit
        ******************************
        """)

    choice = input("Enter your option ")
 
    if choice == "1":
        Name = (input("Enter name of new Employee: "+"\n"))
        Department = (input("Enter Department of Employee: "+"\n"))
        Position = (input("Enter Positon of Employee: "+"\n"))
        rate = int (input("Enter rate of Employee: " + "\n"))

        employees.append(Employee(Name,Department,Position,rate))
        print("Done!")

    elif choice == "2":
          index = int (input("Index no. of Employee: "))
          print(employees[index].name,"is selected!")
          hourly = int (input("Hourly of Employee: "))
          print("Employee's Salary: " , employees[index].rate * hourly)

    elif choice == "3":
        for e in employees:
          print("*********************************")
          print(employees.index(e),"\n","Name:", e.name,"\n","Department:", e.department,"\n","Position:", e.position,"\n","Rate:", e.rate,"\n")
    

    elif choice == "4":
    
          start = False
          print("Exit")

    else:
         print("Invalid number, please try again")
          