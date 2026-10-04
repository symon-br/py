#Functions definition
def calc_Sum(a, b): #Parameters
    return a + b

sum = calc_Sum(1, 4) #Function call with Arguments
print(sum)

# Function is made to reduce the code redundancy and to make the code more modular and reusable.


def No_params():
    print(" ") #Free space; can write anything here.

y= No_params() #Function call without arguments 
print(y) #This will print None because the function does not return anything.


# Question 1

def ave(a, b, c): 
    sum = a + b + c
    average = sum / 3
    print(average) #This will print the average but the function will not return anything, so it will return None by default. If we want to return the average, we should use return statement instead of print statement.
    return average #Only return; no print 

# print(ave(1, 2, 3)) #IN decimal points
# print(int(ave(1, 2, 3))) #IN whole number

ave(1, 1, 1) #Function call


#default parameters
def cal_para(a, b=2): #first parameter is not able to make default as when we call the function, we have to provide value for a and b (i.e. cal_para(1) while the value of a) and if we did def cal_para(a=1, b) then will return SyntaxError: as the default parameter should be at the end of the parameter list.

    print(a * b) #b is a default parameter
    return a * b

cal_para(1) #This will use the default value of b which is 2, so it will return 1*2=2
cal_para(1, 3) #This will override the default value of b and use


# Question 2
#WAF to print the length of the list.
country = ["India", "USA", "UK", "Australia", "Germany", "Nepal", "Bhutan", "Bangladesh", "Sri Lanka", "Pakistan"]

def cal(list):
    print(len(list))
    return len(list)

cal(country)

# Question 3
#WAF to print the elements of a list in a single line
def print_list(list):
    for item in list:
        print(item, end=" ") #end=" " to print all elements in a single line with space between them
    print() #To move to the next line after printing all elements

print_list(country)

#Question 4
# Write 

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
n3 = int(input("Enter a number to find its factorial: "))
print(fact(n3))

# Another way using loops
def fact_loop(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
n5 = int(input("Enter a number to find its factorial using loop: "))
print(fact_loop(n5))



# #Question 5
#WAF to convert inr into npr

def con(n): 
    print(n * 1.6)#1 inr = 1.6 npr
    return n * 1.6
n4 = int(input("Enter amount in INR: "))
con(int(n4))


# Question 6
#WAF to check whether the number is even or odd
def call(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

n6 = int(input("Enter a number to check if it is even or odd: "))
call(n6)





#RECURSIVE function 

def show(n):
    if n > 0:
        print(n)
        show(n - 1) # recursive call 

show(5)

# factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n - 1) * n 
    
n7 = int(input("Enter a number to find its factorial using recursive function: "))
print(factorial(n7))



# write a recursive function to find the sum of first n numbers

def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)
print(sum(5)) #This will return 5 + 4 + 3 + 2 + 1 + 0 = 15



# write a recursive function to find the n number of natural numbers 
def natural(n):
    if n == 0:
        return []
    return natural(n - 1) + [n]
print(natural(5)) #This will return [1, 2, 3, 4, 5]



# write a recursive function to find the n number of natural numbers in reverse order
def con(n):
    if n == 9:
        return []
    return [n] + con(n + 1)

print(con(5))



# Write a recursive function to print all the elements of a list 
def print_list(lst, index=0):
    if index == len(lst):
        return
    print(lst[index])
    print_list(lst, index + 1) # recursive function only if the statement is written inside of the function, otherwise it will return NameError: name 'print_list' is not defined

my_list = [0, 1, 2, 3, 4, 5]
print_list(my_list) #this will print whole function's list which is [0, 1, 2, 3, 4, 5] and the index will be incremented by 1 in each recursive call until it reaches the length of the list.





