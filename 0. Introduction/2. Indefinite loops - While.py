# while and for loops are the same as if
#however, at the end of the function, they always go back and check the condition
#if the condition still met, the repeat the function until the condition is not met

n=5
while n > 0:
    print(n)
    n = n - 1
print("All done")
print("n = " + str(n))

#in the above code, n is called the iteration variable

#------lets create an infinite loop--------#

#if you uncomment the below code block, the program will continue to run forever
#n=5
#while n > 0:
    #print("lather")
    #print("Rinse")
#print("Dry off!")

#------breaking out of a loop------------------#
#use the break statement
print("             ")
print("Testing the break statement...")
print("             ")

n=5
while n > 0:
    print(n)
    n = n - 1
    if n == 2:
        break
print("All done")
print("n = " + str(n))

#--------Finishing an iteration with "continue"------#
#the difference between "break" and "Continue": is that:
#"continue" stops the iteration and goes back to the top (verify the condition again)
#"break" break out of the loop. in the above example it goes to print("All done")
print("             ")
print("Testing the continue statement...")
print("             ")

n=5
while n > 0:
    print(n)
    n = n - 1
    if n == 2:
        continue
    print("ok")
print("All done")
print("n = " + str(n))

# You can see in the output, the loop didn't print "OK" when n==2
#continue caused it to go back to the while question before printing "ok"
