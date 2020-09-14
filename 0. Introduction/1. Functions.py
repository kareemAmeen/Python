# define and call a simple function

#defining the function
def thing():
    print("hello")
    print("this is just a simple function")

#calling/invoking the function
thing()

#calling the function again
thing()

#defining a function with arguments

def argu_fun(x,y):
    z = x + y
    print(z)
    return(z)


#calling a function with arguments

argu_fun(2,3)
g = argu_fun(5,6)
print(g)

def hello(name):
    print("hello " + name)
    if name == "kareem":
        print("yaaaaay!")
    else:
        print("ok")
#the input function will take the name from the userS
hello(input("enter your name: "))
