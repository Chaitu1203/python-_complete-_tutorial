"""Functions is a block of code which runs only when it is called"""
##function anedhey oka block of code manam eppudu call chasthey appudey run avuthadhi.

from tkinter import _XYScrollCommand
from unittest import result


def my_function():
    print("print hello my function")
my_function()


def chaitanya():
    print("how are you")
chaitanya()


"""PARAMETERS & ARGUMENTS"""
#ex1
def chaitanya(name):
    print(f"hello {name} how are you")
chaitanya("geetha")
chaitanya("ganesh")

#ex2
def chaitanya(name , age):
    print(f"hello {name} how are you")
    print(f"i know your age = {age}")
chaitanya("geetha" , 22)
chaitanya("ganesh" , 10)

"""DEFALUT PARAMETER"""
def chaitanya(name , age = 22):
    print(f"hello {name} how are you")
    print(f"i know your age = {age}")
chaitanya("geetha" )
chaitanya("ganesh" )

def chaitanya(name , age = 22):
    print(f"hello {name} how are you")
    if age > 10:
          print(f"i know your age = {age}")
chaitanya("geetha" )
chaitanya("ganesh" , 10)

"""RETURN VALUE FROM FUCTIONS"""
#functions returns the value ,using return statemnet
def is_adult (age):
     return age >= 10
result = is_adult(10)
print(result)


