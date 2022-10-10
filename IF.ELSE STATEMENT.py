## if & else statement basic 
from email import message


number = 22
if number > 20 :
   print(f"{number} is grater than 20")
elif number == 20:
    print(f"{number} is equal to number")
else:
    print(f"{number}is less than 20")


##TERNARY IF STATEMENTS
 ## it allow to do it simple to have allows in one line.

number = 10
message = "postive" if number > 0 else "0 or negitive"
print(message)

x = -1
if x > 10:
    print(f"{x}is greater then 10")
elif x == 10:
    print(f"{x} equal to 10")
else :
    print(f"{x} less than  10")


