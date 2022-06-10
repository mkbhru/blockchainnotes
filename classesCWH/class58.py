from posixpath import split


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
    @classmethod
    def from_str(cls, string):
        return cls(*string.split("-"))
    @staticmethod #if we want to be function normally as it outside of class  
    def printGood(string):
        print("this is good",string)


o1 = Employee("Radha",3453,"instructor")
o2 = Employee("Radhika",7876,"Student")
o3 = Employee.from_str("RamSita-9989-warrior")

o1.printGood("awesome:)")

""" to keep things precise we use these methods so that only what we need to  use should be created and used """
