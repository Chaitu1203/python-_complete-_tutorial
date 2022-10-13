"""definition:genertors are functions that return traversable objects.
tel: genertors anevi functions adhi traversable objects return chastundhi
generators  produce items one at a time and only when it requried 
generators run along with 'for' loops"""



from turtle import pen


def satabdi():
    yield 1
    yield 2
Values = satabdi()
print(Values.__next__())
print(Values.__next__())

    
# using for loop
def nothing():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


for x in nothing():
    print(x)



# For loop to reverse the string
def rev_str(nothing):
    length = len(nothing)
    for i in range(length - 1, -1, -1):
        yield nothing[i]


for char in rev_str("satabdi"):
    print(char)
    


#whileloop
def something():
    n = 1

    while n <= 10:
        sq = n*n
        yield sq
        n += 1

values  = something()

for x in values :
    print(x)
