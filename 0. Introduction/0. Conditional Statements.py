print ("hello world2")
print ("hello world4")

#this next bit will take an input number from the user
#however, we need to account for bad input, so will use a try...except block
#to try out the user input


try:
    y= input("enter your number: ")
    x = int(y)
except:
    print ("error: please enter numeric input")
    quit()

#the above code will try converting the user input to integer, if it failed
#the code will not blow out, it will rather put -1 into x.
#try testing the code using a name in the user input instead of a number

print(x)

#if and elif statements
if x <2:
    print ("small")
#the next line will implement else if
elif x<10:
    print ("Medium")
else:
    print("large")

print ("all done")
