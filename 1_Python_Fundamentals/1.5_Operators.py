
# PYTHON OPERATORS NOTES

# 1. Arithmetic Operators
# +  Addition
# -  Subtraction
# *  Multiplication
# /  Division (returns float)
# // Floor Division (quotient only)
# %  Modulus (remainder)
# ** Exponentiation (power)

from operator import xor


a= 20
b=4

print("Addition:", a + b)          # 24
print("Subtraction:", a - b)       # 16
print("Multiplication:", a * b)    # 80
print("Division:", a / b)          # 5.0
print("Floor Division:", a // b)  # 5
print("Modulus:", a % b)          # 0 
print("Exponentiation:", a ** 2) # 400

# 2. Comparison Operators
# == Equal to
# != Not equal to
# >  Greater than
# <  Less than
# >= Greater than or equal to
# <= Less than or equal to

# Returns True or False

print(a==b)  # False
print(a!=b)  # True
print(a>b )  # True
print(a<b )  # False
print(a>=b)  # True
print(a<=b)  # False


# 3. Assignment Operators 
# In this case, we can use the operator to assign a value to a variable, and also perform an operation on that variable and assign the result back to it.

# =   Assign value
# +=  Add and assign
# -=  Subtract and assign
# *=  Multiply and assign
# /=  Divide and assign
# //= Floor divide and assign
# %=  Modulus and assign
# **= Power and assign

e= 20
print(e)  # 20

e += 5
print(e)  # 25

e-=3
print(e)  # 22

e*=2
print(e)  # 44

e/=2
print(e)  # 22.0

e//=2
print(e)  # 11.0

e%=3
print(e)  # 2.0

e**=2
print(e)  # 4.0

# 4. Logical Operators
# and -> True if both conditions are True
# or  -> True if at least one condition is True
# not -> Reverses the result

c= True
d= False

print(c and d)  # False
print(c or d)   # True
print(not c)    # False
print(xor(c, d))   # True-----needs to be imported from operator module


# 5. Membership Operators
# in      -> Checks if value exists
# not in  -> Checks if value does not exist

# Example:
# "a" in "apple"  # True

# 6. Identity Operators
# is      -> Same object in memory
# is not  -> Different objects

# Example:
# a is b

# 7. Bitwise Operators
# &  AND
# |  OR
# ^  XOR
# ~  NOT
# << Left Shift
# >> Right Shift