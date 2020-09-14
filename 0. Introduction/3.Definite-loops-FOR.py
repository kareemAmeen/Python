#---------Difference between FOR and WHILE------------#
#**WHILE is used for indifinite loops, loops that will not end unless the
#condition is met
#**FOR is used for definite loops, like going through specific number of cells
#in an excel sheet

for i in [5, 4, 3, 2, 1]:
    print(i)
print("ALL Done")

#in the above code: you see we gave the FOR a LIST of parameters to go through
#this list can be list of anything: it can be strings, files, cells....etc
print("             ")
print("Testing a FOR loop with string list...")
print("             ")

friends = ["kareem", "lobna", "tota"]
for name in friends:
    print("Happy new year " + name)
print("All Done")
#notice that "name" was not a variable, the FOR loop created it automatically
print("             ")
print("             ")
print("Finding largest value loop")
#-------What to use loops for?-----------#
#---Finding the largest value---#

largest_so_far = -1
print("Before: ", largest_so_far)
for num in [12, 41, 12, 3, 74, 13]:
    if num > largest_so_far:
        largest_so_far = num
        print ("largest so far is: ", str(num))
print ("After: ", largest_so_far)

#---Counting (a counter code)---#
print("             ")
print("             ")
print("Counting loop...")

count = 0
print("Before: ", count)
for num in [12, 41, 12, 3, 74, 13]:
    count = count + 1
    print ("Count so far is: ", str(count))
print ("After: ", count)


#---Totalizer (Summing in a loop)---#
print("             ")
print("             ")
print("Totalizer loop...")

total = 0
print("Before: ", total)
for num in [12, 41, 12, 3, 74, 13]:
    total = total + num
    print ("Total so far is: ", str(total))
print ("After: ", total)

#---Finding the Average---#
print("             ")
print("             ")
print("Average loop...")

count = 0
total = 0
print("Before: ", count, total)
for num in [12, 41, 12, 3, 74, 13]:
    count = count + 1
    total = total + num
    print (num, count , total)
print ("After: Average= ", total/count)

#---Filtering a list of inputs---#
print("             ")
print("             ")
print("Filtering loop...")

print("Before")
for num in [12, 41, 12, 3, 74, 13]:
    if num > 20:
        print ("large number ", num)
print ("After")

#---Searching in a list---#
#searching for a specific value and counting how many times it is found
print("             ")
print("             ")
print("Searching loop...")

found = False
count = 0
print("Before")
for num in [12, 41, 3, 12, 3, 74, 13]:
    if num == 3:
        found = True
        count = count + 1
        print (found, num)
print ("Search result is: " , found)
print ("Number of occurances is: " , count)
