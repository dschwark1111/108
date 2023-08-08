#comments on python
#variables

name = "Dottie"
last_name= "Schwark"
age = 42
price = 20.13
found = False

print(name + " "+last_name)
print("My age is: " + str (age))

#conditionals

if age < 100:
    print("don't worry you're still young")
    print("still inside the if")
elif age == 100:
    print("congrats")
else:
    ("you're old")

print("outside the if")

def say_hello():
    print("hello from a function")

def sum(num1, num2):
    total = num1 + num2
    print("the result is " + str(total))
    
    
say_hello()
sum(21, 21)