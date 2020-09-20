'''Before we can work with a file inside Python, we want to tell Python that
we're going to work with that file. This is an act we call opening. It's
not actually reading the file. It's just making the file available to the
code that we're going to write. And so the function that we use is a built-in
function in Python, we pass in the name of the file and whether we're going to
read it or write it'''
#this function is called open() and it gives a file handle
#this statement opens the file "mbox-short.txt" and returns the file handle
#fhand
fhand = open ("mbox-short.txt", "r")
#print(fhand)

#The new line character
stuff = "Hello\nWorld" #the \n establishes a new line in the text
print(stuff)

#open a file and print all lines in that file
xfile = open ("mbox-short.txt", "r")
for line in xfile:
    print(line)

#counting how many lines in a file
xfile = open ("mbox-short.txt", "r")
count = 0
for line in xfile:
    count= count+1
print("line count is: ", count)

#reading the entire file into a single string
#then countring how many characters in that string

fhand = open ("mbox-short.txt")
inp = fhand.read()
length = len(inp)
print ("Number of characters in the file is: ", length)
print (inp[:20]) #prints the first 20 characters of inp

#searching through a file
fhand = open ("mbox-short.txt")
for line in fhand:
    line = line.rstrip() #to remove the white spaces from the line
    if line.startswith("From"):
        print(line)
