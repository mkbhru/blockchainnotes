class Employee:
    no_of_leaves = 8

    def __init__(self,name, salary,role):#constructor
        self.name=name
        self.salary=salary
        self.role=role
    
    def printdetails(self):#therefore self represents calling instance or object, it is used to handle
        #automatically passed argument of calling instance
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

o1 = Employee("Radha",3453,"instructor")
# o2 = Employee()

# o1.name = "Radha"
# o1.salary = 3434
# o1.role = "instructor"

# o2.name = "Radhika"
# o2.salary = 23333
# o2.role = "Student"

print(o1.printdetails())










#parameter are at the time defining the function and arguments passed at the time calling a function