'''
b = 7 
c = "hello"
d = 3.14
e = [1, 2, 3]
f = 'i'
A = 7 
print(A)
print(b) 
'''

# g = int(c) # This will raise a ValueError because "hello" cannot be converted to an integer

#print(type(c))



#print(a, b, c, d, e, f)
#print(type(a), type(b), type(c), type(d), type(e), type(f))



# x ="something"

def myfunc():
    y = "awesome"
    print("python is " + y) # this is local variable

myfunc()
print("python is " + x) # this is global variable


def myfunc2():
    global x
    x = "fantastic"

myfunc2()
print("python is " + x) # now this will become global variable


#greater number 
global x
x = "fantastic"

def myfunc2():
    global x
    x = "amazing"  # Example modification

myfunc2()
print("python is " + x)  # now this will become global variable

# Python equivalent of the second block
num1 = 5
num2 = 10
if num1 > num2:
    print("num1 is greater")
else:
    print("num2 is greater")


'''
print("Enter your favorite car:")  #user
favorite_car = input()             #input
print("Your favorite car is " + favorite_car)
# '''
# mylist = ["hayabusa", "ferrari", "lamborghini", "porsche"] #access list example
# print("But My favorite car is " + mylist[-1])  # Accessing the last element using negative indexing



