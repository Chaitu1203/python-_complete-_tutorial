"""An Exception is an error that happens during the execution of a program"""
from ast import Try


y = 10
print(y/0)
"""telugu:while we are writing programme step by step instrution anevi esthu vuntam, 
suupose manam echey instructions anedhi correct ga lekapothey error raise chestundhi ah error ni exception antaru"""

#EXCEPTION HANDLING: When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

"""important terms
The (try) block lets you test a block of code for errors.
tel: block of code lo error vundhi or ledho check cheyadaniki

The (except) block lets you handle the error.
tel:error ni handle cheyadaniki except anedhi use avutundhi"""

try:
  print(5/0)
except:
  print("An exception occurred")

#The (else) block lets you execute code when there is no error.
#tel: error em lekapothey code run avutundhi
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#2
#The try block will generate a NameError, because x is not defined:
try:
  print(y)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

#The (finally) block lets you execute code, regardless of the result of the try- and except blocks.
#ella vunna code run avutundhi
try:
  print(y)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

#2
#The try block will raise an error when trying to write to a read-only file:
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  



#(Raise) a Python developer you can choose to throw an exception if a condition occurs.
#Raise : exception (means its allways through error)
y = -1
if y < 0:
  raise Exception("Sorry, no numbers below zero")

#2
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")


#(assert) insted of waiting for a prograam to a crash midway,you can also start by making an assertion ijn python.
#Assert : test if,condition is true
#tel:condition correct ithey ney e code run avutndhi
import sys
assert ('linux'in sys.platform),"this code runs on linux only."

"""single line word about try,except,raise,finally"""
#Try : run this  coode
#except : excute the code when there is an error
#Else : no exceptions? run this code
#Finally : always run code






