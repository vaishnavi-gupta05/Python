# # STRING METHODS----->>>

# # strings are immutable
# str= "hello world"
# str[0]= "P" #cannot happen because of immutable nature of string

# Methods and functions--->>>

# # length of the string
# str=" hello world"
# a= len(str)
# print(a)

# #CHANGING CASES-->>

# # uppercase all characters
# print(str.upper())
# print(str)  #original string is still same

# # lower case all the characters
# print(str.lower())

# # capitalize the first character
# print(str.capitalize())

# # title-->> capitalize every fisrt charater in the string after space
# print(str.title())

# # REMOVING WHITESPACE--->>

# text= " hello world "
# print(text.strip())  #"hello world"-->> remove all starting and ending space and new lines.

# print(text.lstrip()) #"hello world "-->> remove all left side space and new lines.

# print(text.rstrip()) #" hello world"-->> remove all right side space and new lines.

# # FINDING AND REPLACING--->>

# text= "Python is fun"
# print(text.find("on"))  # find the index of 1st occurance.
# print(text.replace("is", "are")) #will convert all the "is" occurance to "are"


# # SPLITING AND JOINING

# text= "apple,banana,orange"
# print(text)

# split_fruits= text.split(",") #output will be a list
# print(split_fruits)


# join_fruits = ",".join(split_fruits)  #convert the list back to string
# print(join_fruits)

# # CHECKING STRING PROPERTIES

# text= "Pyhton123"
# # true or false
# print(text.isalpha())    #true if all alphabets
# print(text.isdigit())    #true if digits
# print(text.isalnum())    #true if alpha-numeric
# print(text.isspace())    #true if whitespace

# # OTHER

# print(ord("A"))   #ASCAI value
# print(chr(65))    #Visa versa











