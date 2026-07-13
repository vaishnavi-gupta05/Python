# LOOPS

# for loop is used to iterate over a sequence (like a list, tuple, string) or other iterable objects.

for i in range (1,6):  # range(start, stop) - generates numbers from start to stop-1
  print(i)
# Output: 1 2 3 4 5

# print Table of 5
number= 5

for i in range (1,11):
  print("5 X",i,"=",number*i)

# while loop is used to execute a block of code repeatedly as long as a condition is true.

# count=1

# while(count<=5):
#   print(count)
#   count+=1 # Increment count to avoid infinite loop

# print Table of 5 using while loop

count = 1
while (count<=10):
  print("5 X",count,"=",number*count)
  count+=1

