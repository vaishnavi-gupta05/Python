
# CONDITIONAL STATEMENTS

# Used to make decisions in a program based on conditions.

# 1. if Statement
# Executes code if condition is True

# Syntax:
# if condition:
#     statement

# 2. if-else Statement
# Executes one block if condition is True,
# otherwise executes another block.

# Syntax:
# if condition:
#     statement1
# else:
#     statement2

# 3. if-elif-else Statement
# Checks multiple conditions.

# Syntax:
# if condition1:
#     statement1
# elif condition2:
#     statement2
# else:
#     statement3

# 4. Nested if
# An if statement inside another if statement.

# Syntax:
# if condition1:
#     if condition2:
#         statement

# Important:
# Indentation (spaces) is mandatory in Python.
# Conditions return True or False.

# Comparison Operators:
# ==, !=, >, <, >=, <=

# Logical Operators:
# and, or, not


age= int(input("Enter your age: "))

if(age>=18):
    print("You can drive")
else:
    print("You cannot drive")

print("End of programme")



