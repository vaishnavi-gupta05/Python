# print("Q-01")

# num= int (input("Enter your number: "))
# # if-elif-else statement to check if the number is positive, negative or zero
# if(num>0):
#   print("Positive")
# elif(num<0):
#   print("Negative")
# else: print("zero")


# print("Q-02")
# # Check if a number is even or odd
# num= int (input("Enter your number: "))
# if (num%2==0):
#   print("Even")
# else: print("Odd")


# print("Q-03")
# # match-case statement to print the day of the week based on a number input (1-7)

# day= int (input("Enter day number (1-7): "))

# match day:
#   case 1:
#     print("Monday")
#   case 2:
#     print("Tuesday")
#   case 3:
#     print("Wednesday")
#   case 4:
#     print("Thursday")
#   case 5:
#     print("Friday")
#   case 6:
#     print("Saturday")
#   case 7:
#     print("Sunday")
#   case _:
#     print("Invalid day number")

# print("Q-04")
# # Simple calculator using match-case statement to perform basic arithmetic operations based on user input

# num1= int (input("Enter your number: "))
# num2= int (input("Enter your number: "))
# operator= input("Enter operator (+, -, *, /): ")

# print("Result: ", end="")
# match operator:
 
#   case "+":
#     print(num1 + num2)
#   case "-":
#     print(num1 - num2)
#   case "*":
#     print(num1 * num2)
#   case "/":
#     if num2 != 0:
#       print(num1 / num2)
#     else:
#       print("Cannot divide by zero")
#   case _:
#     print("Invalid operator")

# print("Q-05")
# # Calculate the sum of the first 100 natural numbers using a for loop and print the result.

# sum=0
# n= int (input("Enter a number: "))
# for i in range (1, n+1):
#   sum+=i

# print("Sum of first", n, "natural numbers is:", sum)

# print("Q-06")
# # print the pattern
# # *
# # **
# # ***
# # ****
# # *****

# for i in range (1, 6):
#   print("*"*i)

# # using nested loop

# for i in range(1,6):
#   for j in range(1, i+1):
#    print("*", end="")
#   print()  # Move to the next line after each row

# # print("Q-07")
# # Write a program that continuously prompts the user to enter a password until they enter the correct one. Use a while loop to achieve this.

# correct_password= "python123"
# password= input("Enter your password: ")

# while(password!=correct_password):
#   print("Incorrect password. Try again.")
#   password= input("Enter your password: ")

# print("Password correct. Access granted.")

# print("Q-08")
# # use while loop to reverse a number entered by the user and print the reversed number.

# num= int (input("Enter a number: "))
# reversed_num=0
# while(num>0):
#   digit= num%10  #get the last digit
#   reversed_num= reversed_num*10 + digit  #append the last digit to the reversed number
#   num//=10 #remove the last digit

# print("Reversed number is:", reversed_num)

