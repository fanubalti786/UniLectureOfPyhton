#1. For Loop: The for loop in Python is used to iterate over a sequence 
#(such as a list, tuple, string, or range) or any other iterable object.
#It executes a block of code repeatedly until the iteration is complete.


# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
 print(fruit)
# Iterate over a range
for i in range(5):
 print(i)



#While Loop: The while loop in Python is used to execute a block of code repeatedly as
#long as a specified condition is true. 
#Example:
 

# Using while loop to print numbers from 1 to 5
num = 1
while num <= 5:
 print(num)
 num += 1


#Break Statement: 
#The break statement is used to exit a loop prematurely based on a certain condition. Example:

# Using break to stop the loop when 'banana' is encountered
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
 print(fruit)
 if fruit == "banana":
  break


#Continue Statement:
#The continue statement is used to skip the rest of the code inside a loop for the current iteration and
#continue with the next iteration.
#Example:
   

# Using continue to skip printing 'banana'
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
 if fruit == "banana":
  continue
 print(fruit)

#Defining Functions:
# Description: Functions in Python are defined using the def keyword. They allow you
#to encapsulate reusable pieces of code.
#Example:
 
def greet(name):
 print("Hello, " + name + "!")
greet("Alice")

#Function Parameters:
#Description: Parameters are variables that are passed to a function when it is called.
#Example:


def add(x, y):
 return x + y
result = add(3, 5)
print("Result:", result)


#Return Statement:
#Description: The return statement is used to return a value from a function.
#Example:


def multiply(x, y):
 return x * y
result = multiply(3, 5)
print("Result:", result)


#Default Parameters:
#Description: Default parameters allow you to specify default values for function
#parameters.
#Example:

def greet(name="World"):
 print("Hello, " + name + "!")
greet("Alice")
greet()

#Variable-Length Arguments (*args and **kwargs):
#Description: You can define functions that accept a variable number of arguments
#using *args and **kwargs.
#Example:

def sum_all(*args):
 total = 0
 for num in args:
  total += num
  return total
result = sum_all(1, 2, 3, 4, 5)
print("Result:", result)


#Docstrings:
#Description: Docstrings are used to provide documentation for functions.
#Example:

def greet(name):
#This function greets the person with the given name.
 print("Hello, " + name + "!")
help(greet)


