#A string is a data structure that has indexable data within it
#meaning it is basically a LIST data structure with letters as list members

#lets define a string variable
fruit = "banana"
letter = fruit[0]
print(letter)

#The above code will print "b" which is the first letter in banana
#so by using the double brackets [], we could access the individual letters
#of the list

x = 3
w = fruit[x-1]
print(w)
print("              ")
#----String functions------#
#get a length of a string
fruit="banana"
x = len (fruit)
print(x)

#loop through a string
print("              ")
print("loop through a string")
print("              ")

fruit="banana"
for letter in fruit:
    print(letter)

#how many letter "a" is in a word
print("              ")
print("counting letter a")
print("              ")

fruit="banana"
count = 0
for letter in fruit:
    if letter == "a":
        count = count + 1
        print(count)
print("Number of a's = ", count)

#slicing Strings (to grap a piece of the string)
print("              ")
print("Slicing a string")
print("              ")
s = "Monty Python"
print (s[0:4]) #note that this will not include 4, it is up to but not include
print (s[6:7],".")
print (s[6:20])
print (s[:2]) #eliminates element 2 and all elements after that
print (s[8:]) #eliminates all elements after the 8th element
print (s[:]) #prints the entire string
