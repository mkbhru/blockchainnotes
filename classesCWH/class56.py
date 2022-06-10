class Employee:
    no_of_leaves = 8

    def __init__(self,name, salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves=newleaves

o1 = Employee("Radha",3453,"instructor")
o2 = Employee("Radhika",7876,"Student")

o1.change_leaves(66)#because it changes classmethod class is passed as first argument and get changed it not changing instance attributes
print(o1.no_of_leaves)
print(o2.no_of_leaves)