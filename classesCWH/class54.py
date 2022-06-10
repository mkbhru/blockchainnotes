class Employee:
    no_of_leaves = 8
    pass


o1 = Employee()
o2 = Employee()

o1.name = "Radha"
o1.salary = 3434
o1.role = "instructor"

o2.name = "Radhika"
o2.salary = 23333
o2.role = "Student"

print(Employee.no_of_leaves)
print(Employee.__dict__)
Employee.no_of_leaves = 9
o1.no_of_leaves = 100
print(o1.__dict__)
print(o1.no_of_leaves)
""" you can access class variables with instance but can't change class variable using instance, if you 
try to do so you endup getting an extra property (local to instance ) will be added, you can see it by
using .__dict__ attribute"""
#a new instance variable of o1 will be created as no_of_leaves
