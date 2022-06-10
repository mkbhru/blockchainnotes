def greet(): print("how do you do")


greet()


def greet(name):
    print("hello", name)
    print("How do you do!")


greet("Manish")


def add_numbers(num1, num2):
    print("The sum is ", num1+num2)


num1 = 3.7
num2 = 6.4
# we getting 10.1000..1 because of floating point representation error, it happening due to carry maybe
add_numbers(num1, num2)
print("this sting is awesome")