#even or odd number:
number = int(input("enter your number in terminal after code run:"))
if(number%2) == 0:
    print("{0} is even number".format(number))
else:
        print("{0} is odd number".format(number))

#prime number or not:

num = 322
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           break
   else:
       print(num,"is a prime number")


#SWapping
x = "Chaitanya"
y = "luke"
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
# code to swap 'x' and 'y'
x, y = y, x
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)

# Fibonacci 
#A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....
#The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms.
#  This means to say the nth term is the sum of (n-1)th and (n-2)th term.
num = 100
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

#leap year(TASK)
year = 3025
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))


#palindrome (either number or word)
#palindrome number means if we see both from front&back it will look like same is called palindrome

n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")


#Reversing the Number
#means it reverse the hole number from back to front
num = 123456789
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10
print("Reversed Number: " + str(reversed_num))


#perfect number(TASK)
#A perfect number is a number in which the sum of the divisors of a number is equal to the number.
n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print(" Perfect number!")
else:
    print(" not a Perfect number!")

#Sum of digit(TASK)
#The sum() method is used to compute the sum of digits of a number in python in a list.
n=int(input("Enter a number:"))
tot=0
while(n>0):
    dig=n%10
    tot=tot+dig
    n=n//10
print("The total sum of digits is:",tot)


#palindrome (either number or word)
#palindrome number means if we see both from front&back it will look like same is called palindrome

string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")

#Reversing the string

# Python code to reverse a string
# using reversed()
# Function to reverse a string
def reverse(string):
    string = "".join(reversed(string))
    return string
  
s = "Geeksforgeeks"
  
print("The original string is : ", end="")
print(s)
  
print("The reversed string(using reversed) is : ", end="")
print(reverse(s))