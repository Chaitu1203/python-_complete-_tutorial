#Dictionary Methods
#Python has a set of built-in methods that you can use on dictionaries.

"""
Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""


#Create and print a dictionary:

person = {
  "name": "chaitanya",
  "age": "20",
  "from": "india"
}
print(person)

#Print the "brand" value of the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#Remove all elements from the car list:
#The clear() method removes all the elements from a dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)

#Copy the car dictionary:
#The copy() method returns a copy of the specified dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.copy()
print(x)

#Create a dictionary with 3 keys, all with the value 0:
#The fromkeys() method returns a dictionary with the specified keys and the specified value.
x = ('name1', 'name2', 'name3')
y = 0
names = dict.fromkeys(x, y)
print(names)

#get()
#Get the value of the "model" item:
person = {
  "name" : "chiatnaya",
  "age" : "22",
  "adress" : "india"
}
x = person.get("age")
print(x)

#example 2
#Try to return the value of an item that do not exist:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("price", 15000)
print(x)

#items()
#Return the dictionary's key-value pairs:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x)

#example2
#When an item in the dictionary changes value, the view object also gets updated:
person = {
  "name" : "chiatnaya",
  "age" : "22",
  "adress" : "india"
}
x = person.items()
person["adress"] = "us"
print (x)

#keys()
#The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
#Return the keys:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x)

#example2
#When an item is added in the dictionary, the view object also gets updated:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
car["color"] = "white"
print(x)

#pop()
#Remove "model" from the dictionary:
#The pop() method removes the specified item from the dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)

#example2
#The value of the removed item is the return value of the pop() method:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.pop("model")
print(x)

#popitem()
#Remove the last item from the dictionary:
#The popitem() method removes the item that was last inserted into the dictionary.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print(car)

#example2
#The removed item is the return value of the pop() method:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.popitem()
print(x)

#setdefault()
#The setdefault() method returns the value of the item with the specified key.
#Get the value of the "model" item:
person = {
  "name" : "chiatnaya",
  "age" : "22",
  "adress" : "india"
}
x = person.setdefault("age","something")
print(x)

#eaxmple2
#Get the value of the "color" item, if the "color" item does not exist, insert "color" with the value "white":
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "white")
print(x)

#update()	 
#Updates the dictionary with the specified key-value pairs
person = {
  "name" : "chiatnaya",
  "age" : "22",
  "adress" : "india"
}
person.update({"color" : "white"})
print(person)

#values()	
#Returns a list of all the values in the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)

#example2
#When a values is changed in the dictionary, the view object also gets updated:
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
car["year"] = 2018
print(x)

