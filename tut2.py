numbers = range(5)  # 0,1,2,3,4
print(numbers)
i = 1
while i <= 5:
    print(i*'*')
    i += 1
for item in range(5):
    print(item)
marks = [12, 33, 55, "meh"]
print(marks[0:2])
for score in marks:
    print(score)
marks.append(99)
marks.insert(1, 43)
print(marks)
print(99 in marks)
print(len(marks))
print("marks list with the help of while")
i=0
while i < len(marks):
    print(marks[i])
    i += 1
marks.clear()
print(marks)
