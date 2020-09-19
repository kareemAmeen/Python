'''Before we can work with a file inside Python, we want to tell Python that
we're going to work with that file. This is an act we call opening. It's
not actually reading the file. It's just making the file available to the
code that we're going to write. And so the function that we use is a built-in
function in Python, we pass in the name of the file and whether we're going to
read it or write it'''
#this function is called open() and it gives a file handle

fhand = open ("C:\Users\karee\OneDrive\2. Learning\0. Tech Development\Computer Science - Python\Python\1. Data Structures\Files\mbox-short.txt", r)
