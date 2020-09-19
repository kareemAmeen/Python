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

r = fruit.replace("ree" , "nnn")
print (r)

#how to strip white spaces from a test
#a str class library can be used for that. the library name is strip
greet = "    Hello Kareem    "
print(greet)
x = greet.lstrip() #strips left spaces
print(x)
x = greet.rstrip() #strips right spaces
print(x)
x = greet.strip() #strips all white spaces
print(x)

print("              ")
print("              ")

#find a prefix
line = "please have a nice day"
answer = line.startswith("please") #asks if line starts with "please"
print(answer)
answer = line.startswith("P") #asks if line starts with capital P
print(answer)

print("              ")
print("              ")

#slicing data
#we need to get the host of a sent email
data = "From kareem.aameen@gmail.com Sat Jan 5 09:14:16 2008"
#find where the "@" is in data
atpos = data.find("@")
#find where a space comes after the first @
sppos = data.
