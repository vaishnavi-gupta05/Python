
# Break, Continue, and Pass Statements

# 1. Break Statement
# Used to exit a loop prematurely when a certain condition is met.

print("Using Break Statement:")
for i in range(1, 10):
    print(i)
    if i == 5:
        break  # Exit the loop when i is 5
    
# 2. Continue Statement
# Used to skip the current iteration of a loop and continue with the next one.

print("\nUsing Continue Statement(for skipping 5):")
for i in range(1, 10):
    if i == 5:
        continue  #loop will continue from here itself when i is 5, so 5 will not be printed because print statement is after continue statement
    print(i)  # This will print all numbers from 1 to 9 except 5


print("\nUsing Continue Statement(for keeping 5):")
for i in range(1, 10):
    print(i) 
    if i == 5:
        continue  # loop will continue from here itself when i is 5, so 5 will be printed because print statement is before continue statement

# 3. Pass Statement
# Used as a placeholder when a statement is required syntactically but no action is needed. 

print("\nUsing Pass Statement:")
for i in range(1, 10):
    if i == 5:
        pass  # Do nothing when i is 5
    print(i)  # This will print all numbers from 1 to 9 including 5