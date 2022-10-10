"""
1.class & objects
2.inheritence
3.polymorphism
4.abstraction
5.encapusulation"""

#CLASSES & OBJECTS:
 # clases is an blueprint to create an object.

from mimetypes import init
from typing_extensions import Self


class car():
    pass

honda = car()
tata = car()

honda.brand = 'bolt'
honda.year = 2016
honda.price = 100000


tata.brand = 'city'
tata.year = 2018
tata.price = 600000
print(honda.price)


class car():
    def __init__(self,modelname , year , price):
        self.modelname = modelname
        self.year = year
        self.price = price

honda = car('city', 2018 , 100000)
tata = car ('bolt' , 2016 , 200000)

print(tata.__dict__)
    

# adding values & and increasing salary method
class car():
    def __init__(self,modelname , year , price):
        self.modelname = modelname
        self.year = year
        self.price = price
    def price_inc(self):
        self.price = (self.price+200000)

honda = car('city', 2018 , 100000)
tata = car ('bolt' , 2016 , 200000)

print(tata.price)
tata.price_inc()
print(tata.price)

##class & object example
class chaitanya:
    d=12
    def display(self):
        a=10
        b=20
        print(a,b)
obj=chaitanya()
obj.display()
print(obj.d)

## construtor
class mobile:
    def __init__(self,brand,price,camera):
        self.brand = brand
        self.price = price
        self.camera = camera
    
oppo = mobile("apple",200000,"40mp")
vivo = mobile("orange",20000,"20mp")
# for i in range(5): to print multiple times
print(oppo.__dict__)
#print("-----------------") to separate the lines
print(vivo.__dict__)

##object method using myfunction
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


##INHERITENCE:
"""the method of inheriting the properties of parents class into a child class is known as inheritence"""
"""SINGLE INHERITENCE"""
#direct parents to child
class parent:
    def fun1(self):
        print("this is parent class")
class child(parent):
    def fun2 (self):
        print("this is a child class")
obj = child()
obj.fun1()
obj.fun2()

## MULTIPLE INHERITENCE
#parent==> child ==> grandchild
class parent:
    def fun1(self):
        print("this is parent class")
class child(parent):
    def fun2 (self):
        print("this is a child class")
class Grandchild(child):
    def fun3 (self):
        print("this is a grand child class")
obj = Grandchild()
obj.fun1()
obj.fun2()
obj.fun3()

#hirarical inheritence
#single parent two children, hear properties belongs to single child
class parent:
    def fun1(self):
        print("this is parent class")
class child1(parent):
    def fun2 (self):
        print("this is a child1 class")
class child2(parent):
    def fun3 (self):
        print("this is a child2 class")
obj = child1()
obj.fun1()
obj.fun2()
#obj.fun3()


##multiple inheritence
#two parents to child , means father-mother==>child
class Father:
    def fun1(self):
        print("this is father class")
class Mother():
    def fun2 (self):
        print("this is a mother class")
class child(Father,Mother):
    def fun3 (self):
        print("this is a  child class")
obj = child()
obj.fun1()
obj.fun2()
obj.fun3()

"""super keyword"""
#parent class lo vuanvi child class lo ki acess chesukovadaniki super() keyword anedhi use avuthadhi
class A:
    def __init__(self):
        print("this is class a")
    
    def fun1(self):
        print("this is a father class")
class B(A):
    def __init__(self):
        print("this is a class b")
        super().__init__()
    def fun2(self):
        print("this is a mother class")

obj=B()
        
"""POLYMORPHISM"""
#Polymorphism is taken from the Greek words Poly (many) and morphism (forms). 
# It means that the same function name can be used for different types
"""METHOD OVERLOADING"""
#method name will be same but parameter will be different
#name will be same but data type will be differnt.
"""
same class
same function or method names
differen parameter
"""
class A():
    def sum (self,a,b):
        return a+b
    def sum (self,a,b,c):
        return a+b+c
    def sum (self,a,b,c,d,e):
        return a+b+c+d+e

obj = A()
print(obj.sum(1,3,5,5,1))
 
#METHOD OVERRIDING
"""different classes
same functio or method names
different parameters
"""
class A():
    def sum (self):
        print("this is a class A")
class B(A):
    def sum (self):
        print("this is a class B")
        super().sum()
obj = B()
obj.sum()


"""ENCAPUSULATION"""
#wrapping up of data under single unit (methods & variable combine in a single place is called encapusulation)
"""
encapusulation have some specifiers
private ==> only inside the class & class method
public == > entire prograam 
protected ==> inside  class and its immediate sub class
"""
class Robo:
    x = 100 #this is public 
    def sum(self):
        print("this is chaitanya")

obj = Robo()
obj.sum()
print(obj.x)


##private (__)
#it only print inside the class and inside the variable
class Robo:
    __x = 100 
    def sum(self):
        print(self.__x)

obj = Robo()
obj.sum()
print(obj.x)

"""ABSTRACTION"""
#means handling unneccesery details showing esstional details.

#abstract class: if a class contains atleast on abstract method
#abstract method: a method without definition
#concrate class: if a class doesnot abstract method..
"""1.we cannot create an object for abstract class.we can create an object for concrate class
2. to convert abstract class to concreate class using inheritence concept
3.to implement abstract class into abstract method we need to import module abc """
from abc import ABC , abstractmethod
class Robo(ABC):
    @abstractmethod
    def sana(self):
        None
class chitti(Robo):
    def sana(self):
        print("haisana")
obj = chitti()
obj.sana()






















