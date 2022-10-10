## sets are used to store multiple items in a single variable.
# sets is some what similar to list but dupplicates are not allowed.
# un orderd & duplicate

number_set = {1, 1}
print (number_set) # duplicates are not allowed.

#ADD : The add() method adds an element to the set.

x ={"A" , "B" , "C" , "D"}
x.add("Z")
print(x)

##CLEAR : clear all the elements in x set.

x ={"A" , "B" , "C" , "D"}
x.clear()
print(x)

#COPY:returns the copy of same set

x ={"A" , "B" , "C" , "D"}
x.copy
print(x)

#DISCARD : method removes the specified item from the set.

x ={"A" , "B" , "C" , "D"}
x.discard("B")
print(x)

##POP : remove a random item from set

fruits = {"apple" , "banana" , "kiwi"}
fruits.pop()
print(fruits)

##UNION :union just takes everything from both sets and put it inside another set. 

A = {"A" , "B" , "C" , "D"}
B = {"E" , "F" , "G"}
C = A.union(B)
print (C)

## set INTERSECTION : intersection method returns a set thst contains the common b/w sets 

x ={"A" , "B" , "C" , "D"}
y = {"E" , "F" , "G",  "A"}
z = x.intersection (y)
print(z)

##difference:  The returned set contains items that exist only in the first set, and not in both sets.


x ={"A" , "B" , "C" , "D"}
y = {"E" , "F" , "B",  "A"}
z = x.difference(y)
print(z)

## ISSUPERSET: method returns True if all items in the specified set exists in the original set, otherwise it retuns False.
"""y set lo vunna items x set lo vuntey adhi true , ledha false"""

x = {"a", "b", "c", "d", "e", "f"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)


#issubset(): method returns True if all items in the set exists in the specified set, otherwise it retuns False
"""x set  lo vunna items y set lo kuda vuntey adhi true ledha false"""
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)


## ISDISJOINT : method returns True both x , y value  doesn't have similar items it shows true, else flase

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)





