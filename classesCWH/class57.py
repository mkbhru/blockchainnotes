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
        # params=string.split("-")
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))# star unpacks list and passes them as individual arguments

o1 = Employee("Radha",3453,"instructor")
o2 = Employee("Radhika",7876,"Student")
o3 = Employee.from_str("RamSita-9989-warrior")

o1.change_leaves(66)

print(o3.role)