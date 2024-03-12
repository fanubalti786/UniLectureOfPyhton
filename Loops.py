# #1. For Loop: The for loop in Python is used to iterate over a sequence 
# #(such as a list, tuple, string, or range) or any other iterable object.
# #It executes a block of code repeatedly until the iteration is complete.


# # Iterate over a list
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#  print(fruit)
# # Iterate over a range
# for i in range(5):
#  print(i)



# #While Loop: The while loop in Python is used to execute a block of code repeatedly as
# #long as a specified condition is true. 
# #Example:
 

# # Using while loop to print numbers from 1 to 5
# num = 1
# while num <= 5:
#  print(num)
#  num += 1


# #Break Statement: 
# #The break statement is used to exit a loop prematurely based on a certain condition. Example:

# # Using break to stop the loop when 'banana' is encountered
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#  print(fruit)
#  if fruit == "banana":
#    Break


# #Continue Statement:
# #The continue statement is used to skip the rest of the code inside a loop for the current iteration and
# #continue with the next iteration.
# #Example:
   

# Using continue to skip printing 'banana'
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
 if fruit == "banana":
  continue
  print(fruit)
