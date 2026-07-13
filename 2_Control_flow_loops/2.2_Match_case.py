# MATCH-CASE 

# Used as an alternative to multiple if-elif-else statements.
# Matches a value against different patterns.

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")   # Default case

# Multiple values in one case
grade = "A"

match grade:
    case "A" | "B":
        print("Excellent")
    case "C":
        print("Good")
    case _:
        print("Needs Improvement")

# Match with conditions (guard)
age = 20

match age:
    case x if x >= 18:
        print("Adult")
    case _:
        print("Minor")

# Key Points:
# 1. Introduced in Python 3.10
# 2. Similar to switch-case in other languages
# 3. '_' acts as the default case
# 4. Can match multiple values and conditions
# 5. Makes code cleaner and more readable