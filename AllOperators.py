# Comparison operators

x = 10
y = 20
# equal to
print("Equal to:",x==y)

# Not equal to
print("Not equal to:", x!=y)

# Greater than 
print("Greater than:", x>y)

# less than
print("Less than:", x<y)

# Greater than or equal to 
print("Greater than or equal to:", x>=y)

# Less than or equal to 
print("Less than or equal:", x<=y)


# Lolgical Operators

def logical_operations(x,y):
  logical_and_result = x and y
  logical_or_result = x or y
  logical_not_result_x = not x
  logical_not_result_y = not y
  return logical_and_result, logical_or_result, logical_not_result_x, logical_not_result_y

x = True
y = False

print(logical_operations(x,y))

x = True
y = False

# Logical AND
print("Logical AND:", x and y)

# logical Or
print("Logical OR:", x or y)

# Logical NOT
print("Logical NOT:", not x)

# Assingment Operators:

def assingmen_operators(x,y):
  x +=y
  x -=y
  x *=y
  x /=y
  x %=y
  x **=y

  # return x #addition
  # return x #subtraction
  # return x #multiplication
  # return x #division
  # return x #Modulus
  return x #square
x = 5
y = 6

print(assingmen_operators(x,y))

# Bitwise Operators

def bitwise_operations(x,y):
  bitwise_and_result=x & y
  bitwise_or_result=x | y
  bitwise_xor_result=x ^ y
  bitwise_not_result_x=~x
  bitwise_not_result_y=~y
  bitwise_left_shift_result=x<<2
  bitwise_right_shift_result=x>>2
  
  return bitwise_and_result, bitwise_or_result, bitwise_xor_result, bitwise_not_result_x, bitwise_not_result_y, bitwise_left_shift_result, 
  bitwise_right_shift_result

x = 60
y = 13

print(bitwise_operations(x,y))
