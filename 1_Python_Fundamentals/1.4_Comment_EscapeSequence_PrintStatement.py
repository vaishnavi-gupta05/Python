
# COMMENT--->>

# This is a single line comment

'''
This is a multi line comment
'''

# ESCAPE SEQUENCE--->>
# \n--->> new line
# \t--->> tab

print("hello\nworld") #new line
print("hello\tworld") #tab

# backslash
print("hello\\newline") #prints the backslash and n

# double quotes
print("hello \" world") #prints the double quotes

# PRINT STATEMENT--->>

#prints the two strings with a space in between by default
print("hello world",'welcome to python programming') 

#sep parameter is used to specify what to print between the two strings
print("hello world","welcome to python programming", sep="/") #print two srings with / in between

#end parameter is used to specify what to print at the end of the statement
# by default it is a new line but we can change it to anything we want

print("hello world", end=',') #prints the string and ends with a comma instead of a new line') 
print("welcome to python programming") #prints the string in the same line as the previous print

