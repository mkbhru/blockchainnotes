students=["Ram","Shyam","Radha","Radhika","Krishna"]

for student in students:
    if student =="Shyam":
        continue
    if student == "Krishna":
        break
    print(student)
marks = (23,45,66,44,44,44,44) # tuple, immutable, it can also be defined without Parenthesis
print(marks.count(44))
print(marks.index(66))
markis = {23,44,22,44,44,65}#Set, only stores a value one time, doesn't keep track of indexes
# therefore markis[2] gives error, we can only iterate over it using for, unordered structure
print(markis)
marksDictionary = {"english":34, "maths":23, "physics":88}#dictionary
print(marksDictionary["english"])
