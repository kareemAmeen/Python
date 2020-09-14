#using "in" as a logical condition
#---------------------------------
fruit="banana"
x="n" in fruit #asking if letter "n" is in the work banana
print(x)

y = "nan" in fruit
print(y)

if "a" in fruit:
    print("found it")


#String library
fruit = "kareem"
x = fruit.upper() #upper is a method in the class "str" which is the string class
print(x)
t = type(fruit)
print (t)
t = dir(fruit) #dir gives you all the things that can be done with this class
print (t)

position = fruit.find("ree")
print(position)
