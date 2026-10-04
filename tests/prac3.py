number_of_GF = [2,1,34,5,6,7]
number_of_GF.sort(reverse = True) #reverse=True sortd the list in decending order and normally list order will sorted in acending order
print(number_of_GF)
number_of_GF.append(3) #append() function will add the new value at the end of the list
print(number_of_GF)
number_of_GF.insert(2, 45) #insert() function will add the new value at the given index
print(number_of_GF)


# WAP to ask user to input their three favorite movies and store them in a list and print the list

# --> one way

a = input("Enter your favorite movie :")
b = input("Enter your second favorite movie :")
c = input("Enter your third favorite movie :")
movies = [a, b, c]
print(movies)

#--> another way
movies = []
movies.append(input("Enter your favorite movies :"))
movies.append(input("Enter your second favorite movie :")) 
movies.append(input("Enter your third favorite movie :"))
print(movies)
movies.sort() #this will sort the list in acending order
print("Sorted movies list: ", movies)



# WAP to check if a string is palindrome or not
str1 = input("Enter anything you want: ")
str2 = input("Enter anything you want: ")
if str1 == str2:
    print("The given string is palindrome")
elif str1 != str2:
    print("The given string is not palindrome")

# in list 
list = []
str1 = input("Enter anything you want: ")
str2 = input("Enter anything you want: ")
str3 = input("Enter anything you want: ")
list.append(str1)
list.append(str2)
list.append(str3)
list2 = list.copy()
list2.reverse() #this changes
if list == list2:
    print("The given string is palindrome")
elif list != list2:
    print("The given string is not palindrome")   
print(list)




#WAP to count how many "A" are in a tuple and sort a list of strings
tup = ("A","B","A","C","D","A")
print(tup.count("A")) #this will count how many times A appears in the tuple

list1 = ["A","B","A","C","D","A"]
list1.sort()
print(list1)


# tuple = ()
# list = []
# string = ""