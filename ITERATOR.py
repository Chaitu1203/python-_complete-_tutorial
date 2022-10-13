"""
definition:an iterator is an object which contains number of values,that can be iterated upon
tel:iterator anedhi oka object adhi number of values ni kalligivuntadhi
(iterated upon :means that you can travesd through all the values)

differnce b/w iterable and iterator:
iteerable:list,tuple,dict and sets all are iterable objects
iterator: that iterable objects acts as containers to get the iterator
tel:iterable objects anevi containers la act chesthai enduku antey to get iterator
"""
#example1:
#we can create an iterable object using anything like list,tuple,set....,
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#example : using string
set = "chaitanya"
something = iter(set)

print(next(something))
print(next(something))
print(next(something))
print(next(something))
print(next(something))
print(next(something))
print(next(something))
print(next(something))
print(next(something))

#example3: using loops
set = ["apple", "luke", "chaitanya"]
for x in set:
    print(x)


#creating a custum iterator
#to create a iterator,we need to implement the methods __iter__() & __next__().
class something:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 2
        return x

example = something()
nothing = iter(example)

print(next(nothing))
print(next(nothing))    
#how many numbers we want we can give print

#stopiteration:
class something:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
      if self.a <= 20:
        x = self.a
        self.a += 2
        return x
      else:
        raise StopIteration

example = something()
nothing = iter(example)

for x in nothing:
    print(x)



