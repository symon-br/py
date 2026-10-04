str1 = "Humans are more likely a savages than civilized beings."
str2 = "Symon "," is a good boy"
print(len(str1))
print(len(str2))


# This is slicing operation
a = "naimang"
print(a[1:4])
print(a[:]) # prints the whole string
print(a[-4:-1])


name = input("Enter your name HUMAN: ")
print(len(name),  "is the length of your name.")


str4 = "Hello $ymon with $$$$$!!"
print(str4.count('$')) #This will count the number of times '$' appears in the string

str3 = "Hello  $ymon!!"
print(str3.find('$')) #this will show the index where $ sign is appears. If not found, it will return -1


#CONDITIONAL STATEMENTS
marks = int(input("Enter your makrs:"))

if marks >= 90:
    print("Grade is A")
elif marks >= 80 and marks < 90:
    print("Grade is B")
elif marks >= 70 and marks < 80:
    print("Grade is C")
elif marks >= 60 and marks < 70:
    print("Grade is D")
else:
    print("BE MORE FOCUSED!! YOU ARE FAILING")

# WAP that if user inputs a number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("You entered an even number.")
elif num % 2 != 0:
    print("You entered an odd number.")
else:
    print("You entered some String value, \n please eneter a valid number.")

# Greatest number among 3 which is enter by user 
num = int(input("Enter a first number: "))
num2 = int(input("Enter a second number: "))
num3 = int(input("Enter a third number: "))

if num >= num2 and num >= num3:
    print("The greatest number is: ", num)
elif num2 >=num and num2 >= num3:
    print("The greatest number is: ", num2)
else:
    print("The greatest number is: ",num3)



# WAP to check if a number is multiplied by 7 or not 
num = int(input("Enter a number: "))
if num % 7 == 0:
    print("The number is multiple of 7.")
else:
    print("The number is not multiple of 7.")