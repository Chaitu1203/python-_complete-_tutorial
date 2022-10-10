## STRING IS JUST A "SEQUCENCE OF CHARACTERS".
## IT CAN BE CREATED BY ENCLOSING CHARACTERS IN SINGLE OR DOUBLE QUOTES.


## Example (uppper case)
from unicodedata import name


brand = "Chaitanya"
print (brand.upper())

# REPALCE 
brand = "Chaitanya"
print (brand.replace('C' , ''))

#length
brand = 'chaitanya'
print(len(brand))

## comparing true or flase 
brand = 'Chaitanya'
print(brand == 'chaitanya')
print(brand != 'chaitanya')

# brand in chaitanya is boolen type.
brand = "chaitanya"
print("tanya" in brand)
print('tanya' not in brand)


##MULTILINE & FORMATING STRINGS
## 1st type
name = "chaitanya"
email = f"""
hello {name}
    how are you?
    it was nice talking to you
    age {22}
"""
print(email)
