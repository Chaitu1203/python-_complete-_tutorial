"""With the while loop we can execute a set of statements as long as a condition is true"""
"""ekada manm a number isthamo daniki oka number mundhu answer print avuthundhi"""
from sqlite3.dbapi2 import _Statement


x = 0
while x < 6:
  print (x)
  x +=1


"""BRAEAK STATEMENT"""
##e braeak statement lo manam oka value isthey ahkaditho value braek ipotundhi 

i = 1
while i < 6:
  print (i)
  if i == 3:
    break
  i += 1


  """CONTINUE STATEMENT"""
##manam oka number isthey ah number remove chesi remining continue avuttundhi .

i = 0
while i < 6:
  i += 1
  i == 3
  continue
print (i)

#else _Statement
x = 0
while x < 6:
  print (x)
  x +=1
else:
  print("print the value")
