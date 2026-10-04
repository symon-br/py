#QUESTION 1
# WAP to print numbers from 1 to 100
z = 1
while z <= 100:
    print(z)
    z+=1


#QUESTION 2
# WAP to print numbers from 100 to 1
t = 100
while t >= 1:
    print(t)
    t-=1


#QUESTION 3
# WAP to print multiplication table of a given number
num = int(input("Enter a number: "))
f = 1
while f <= 10:
    print(num, "x", f, "=", num*f)
    f+=1


# QUESTION 4
num2 = [1,4,9,16,25,36,49,64,81,100]

#traverse (means to go through each elements of list)
l = 0
while l <= 9: #len(num)-1
    print(num2[l])
    l+=1


# # QUESTION 5
num3 = (1,4,9,16,25,36,49,64,81,100)

x = int(input("Enter a number to search in the tuple: "))

o = 0
while o < len(num3):
    if num3[o] == x:
        print("Found at index:", o)
    elif num3[o] != x:
        print("finding...")
    o += 1




# "concept of break and continue in python"
#"break"
y = 0
while y < 10:
    if y == 5:
        break  # this will stop the loop when y is 5
    print(y)
    y+=1
print("Loop ended.")

#"continue"
k = 0
while k < 10:
    k += 1
    if k == 5:
        continue  # this will skip the rest of the loop when k is 5
    print(k)
print("Loop ended.")




#"concept of for loop in python"

people = ["symon", "john", "charlie"]
people2 = ("Murphy", "Robert", "leonardo")
str = "leonardo di caprio"

for person in people:
    print("Hello", person) #list print

for person1 in people2:
    print("Fuck off", person1) #tuples print

for char in str:
    print(char) #characters of string print




# "use of else in for loop"
e = ("charlie", "bob", "chart", "joy")
for q in e:
    if(q == "chart"):
      print(q)
      break      #if(q =="char") --> HEHEH "since char is not in tuples"
else:               #else in python  used to make sure that code is fully executed
    print("HEHEH")
    

# QUESTION 1
"list"
num = [1,4,9,16,25,36,49,64,81,100]
for el in num:
    print(el)
else:
    print("WOW!")


#QUESTION 2
"tuples"
num4 = (1,4,9,16,25,36,49,64,81,100)

r= int(input("Enter a number to search in the tuple: "))

for eli in num4:
    if(eli == r):
        print("Found at index:", num4.index(eli))
    else:
        print("Loading...")

#QUESTION 3 
# "dictionary"
d = {
    "name": ": symon",
    "age": ": 20",
    "city": ": kolkata"
}

for u in d:
    print(u, d[u])




# range in python loops
for yh in range(10): #range(stop)
    print(yh)
print("END")

for s in range(3,10): #range(start,stop)
    print(s)

for p in range(3, 10, 2): #range(start,stop,step)
    print(p)

#print all even numbers From zero to ten 
for c in range(0, 10, 2):
    print("even",c)


#use for and range 
#QUESTION 1
# WAP to print 1 to 100
for te in range(1,101):
    print(te)


#QUESTION 2
#WAP to print 100 to 1
for qi in range(101, 0, -1):
    print(qi)


#QUESTION 3
#WAP to print multiplication table  of n 
n1 = int(input("ENTER any number: "))

for pa in range(1,11):
    print(n1 * pa)




# "pass in python"
for ma in range(10):
    pass #Empty




# PRACTICE of loops  
#QUESTION 1
# WAP to find sum of first n numbers (using while)
n2 = int(input("Enter n number: "))
sile = 0
sum = 0
while sile <= n2:
    sum += sile
    sile +=1

print("Total sum is: ", sum)


#QUESTION 2
#WAP to find factorial of first n number(using for)
n3 = int(input("Enter any number: "))
mul = 1
for il in range(1, n3 + 1):
    mul *= il

print(mul)