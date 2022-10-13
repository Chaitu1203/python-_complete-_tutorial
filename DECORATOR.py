"""first_class_object: in pyhton, everything is treated as a object inculding all the data types functions too, 
there fore function is also known as a first class object and can be passed around arguments.."""

def func1 (name):
    return f"{name}Hello"
def func2 (name):
    return f"{name}how you doing?"
def func3 (func4):
    return func4 ('dear learner')
print (func3(func1))
print (func3(func2))

#2.inner_function: it is possible to define functions inside a function,that functiion is called an inner function..

def func():
    print("first function")
    def fun1():
        print("first child function")
    def  fun2():
        print("second child function")
   
    fun2()
    fun1()

#function from  function: 
def func(n):
    def func1():
        return 'edureka'
    def func2():
        return "python"
    if n == 1:
        return func1
    else :
        return func2
a = func(1)
b = func(2)
print(a())
print(b())



#definition: decarator is a function, that takes anthor function is an arugument and add some kinds of functionallity and returns function
#tel: decorater anedhi oka function, ah function inko function ni arugument ga tesukoni koni funcionallities add chesi function return chastundhi.

def div(a,b):
    print(a/b)


def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)

    return inner

div= smart_div (div)

div(2,4)


#1 decorators expample
def function1(function):
    def chaitanya():
        print("Hello")
        function()
        print("welcome to chaitnay's home")
    return chaitanya
def function2():
    print("chaitanyalalam") 

function2 = function1(function2)

function2()


#2 py syntax (or) syntatic sugar
#this mwthodf will use easy to create decorator
def function1(function):
    def chaitanya():
        print("Hello")
        function()
        print("welcome to chaitnay's home")
    return chaitanya
@function1
def function2():
    print("chaitanyalalam")

function2()  

#3 decorators with arguments:
def function1(function):
    def chaitanya(*args , **kwargs):
        print("Hello")
        function(*args , **kwargs)
        print("welcome to chaitnay's home")
    return chaitanya
@function1
def function2(name):
    print(name)

function2("luke")  

"""#4 returning values with decorated function
def function1(function):
    def wrapper(*args , **kwargs):
        print('its worked')
    return wrapper
@function1
def function2(name):
    print(name)
function2("python")
"""