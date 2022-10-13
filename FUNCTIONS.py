"""Functions is a block of code which runs only when it is called"""
##function anedhey oka block of code manam eppudu call chasthey appudey run avuthadhi.

#Python Functions
#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.

#Creating a Function (1)
#In Python a function is defined using the def keyword:
#Example
def my_function():
  print("Hello from a function")


#Calling a Function (2)
#To call a function, use the function name followed by parenthesis:
#Example
def my_function():
  print("Hello from a function")
my_function()


#Arguments(3)
#Information can be passed into functions as arguments.
#Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
#The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
#Example
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")
#Arguments are often shortened to args in Python documentations.

#Parameters or Arguments? (4)
#The terms parameter and argument can be used for the same thing: information that are passed into a function.
#From a function's perspective:
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the value that is sent to the function when it is called.

#Number of Arguments (5)
#By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
#Example
#This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")

#If you try to call the function with 1 or 3 arguments, you will get an error:
#Example
#This function expects 2 arguments, but gets only 1:
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil")


#Arbitrary Arguments, *args(6)
#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments, and can access the items accordingly:
#Example
#If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[1])
my_function("Emil", "Tobias", "Linus")

#Arbitrary Arguments are often shortened to *args in Python documentations.

#Keyword Arguments(7)
#You can also send arguments with the key = value syntax.
#This way the order of the arguments does not matter.
#Example
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
#Arbitrary Keyword Arguments, **kwargs(8)
#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly:
#Example
#If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["fname"])
my_function(fname = "chiatanya", lname = "lalam")
#Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.

#Default Parameter Value(9)
#The following example shows how to use a default parameter value.
#If we call the function without argument, it uses the default value:
#Example
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#Passing a List as an Argument(10)
#You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
#E.g. if you send a List as an argument, it will still be a List when it reaches the function:
#Example
def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#Return Values(11)
#To let a function return a value, use the return statement:
#Example
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#The pass Statement(12)
#function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
#Example
def myfunction():
  pass
#Recursion(12)
#definition: The process in which a function calls itself directly or indirectly is called recursion.
# and the corresponding function is called recursive function.
# take two mirrors parallel to each other.then stand in b/w of them, and you will notice infinite images of yourself within mirrors and thats recurrsion.
#Example
#Recursion Example

def chaitanya(x):
  if(x > 0):
    result = x + chaitanya(x - 1)
    print(result)
  else:
    result = 0
  return result

print("this is chaitanya")
chaitanya(5)



def chaitanya(x):
  if  x == 1:
    return 1
  else:
      return(x * chaitanya(x-1))
num = 4
print("the chaitanya of",num,"is", chaitanya(num))

"""recursion can be infinte
but  if the code does not have specific condition to stop recurrsion, the system might slow down 
hence, python provides recurrsion limit of 1000 only"""

