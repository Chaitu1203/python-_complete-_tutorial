"""A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages"""

## With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
import numbers
from optparse import Values
from unicodedata import name


names = ["Chaitanya" , "raju" , "ramalakshmi" , "geetha", "ganesh"]
for  x in names:
    print(x)
    

"""LOOP THROUGH DICTIONARIES"""

person = {
    "name" : "chaitanya",
    "age"  : 22,
    "from" : "india"
}
print (person.items())


##for loop  excerices
numbers = [1,2,3,4,5,6]


#solution
result = 0
numbers = [1,2,3,4,5,6]

for x in numbers:
    result += x
print(f"reasult = {result}")

"""RANGE FUNCTION"""
#To loop through a set of code a specified number of times, we can use the range() function.
#specified items ni print cheyadamey lo e range function use chestham.
# edhi default kuda 0 nundi start avuthadhi.
for x in range (7):
    print(x)

# example 2
for x in range (2 , 7):
    print(x)

# example 3 
"""first 2 nundi start avuthadhi 38 varaku print avuthadhi 2-2 numbers gap ichee"""
for x in range (2 , 40 , 2):
    print(x)

"""USING IF & ELSE IN LOOP"""
for x in range(6):
  if x == 2: break
  print(x)
else:
  print("Finally finished!")
  
#If the loop breaks, the else block is not executed.