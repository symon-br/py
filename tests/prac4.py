# dictionary in python
info = {
    "name" : "symon",
    "age" : 27,
    12 : "twelve"
}
print(info)

# nested dictionary
student = {
    "key" : "value",
    "name" : "praful",
    "surname" : "sharma",
    "subjects" : {
        "maths" : 78,
        "science" : 88,
        "english" : 90
    }
}
print(student["subjects"]["science"])

student1 = {} #empty dictionary
student1["name"] = "john"
print(student1)


# Methods in dictionary
print(student.get("name2")) #no error -> None
print(student["name"]) #error 

print(list(student.keys())) #prints all the keys in the dictionary in list format
print(student.values()) #prints all the values in the dictionary
print(student.items()) #prints all the key value pairs in the dictionary
print(student.pop("surname")) #removes the key value pair with the given key and returns the value
print(student.update({"name" : "praful sharma"})) #updates the value of the given key

# set in python
# boolean, tuple, string, integer, float are all immutable and can stored in set but list and dictionary are mutable and cannot be stored in set

col = {"red", "green", "blue", 1, 3, 5 }
print(col)
print(type(col))

col1 = set() #empty set; syntax 
col1.add(5)           #{
col1.add(10)          #set add() method adds an element to the set
col1.add(15)          
col1.add("hello")     
print(col1)           #}

col2 = {1,2,3,4,5}
col3 = {4,5,6,7,8}

print(col2.union(col3)) #union() method conbines two sets and removes duplicates
print(col2.intersection(col3)) #intersection() method returns the common elements in both sets
print(col2.clear())#clears the set
print(col2.pop()) #removes and returns a random element from the set
print(col2.remove(3)) #removes the given element from the set


#Question 1
'''WAP to store the following names in dictionary 
table = "piece of furniture", "list of facts and figures"
cat = "a small animal"
'''

dictionary = {
    "table" : ["piece of furniture", "list of facts and figures"],
    "cat" : "a small animal"
}
print(dictionary)

# Question 2
'''WAP to store the following subjects in a set and print the number of unique subjects'''
col = ["python", "java", "c++", "python", "javascript", "java", "python", "java", "c++","c"]

classroom = set(col)
print(classroom)
print("Number of unique subjects in the classroom: ", len(classroom))


# Question 3
'''WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value. (also use set())'''
Entery = input("Enter 1st subject: ")
Entery1 = input("Enter 2nd subject: ")
Entery2 = input("Enter 3rd subject: ")

subjects = set()
subjects.add(Entery)
subjects.add(Entery1)
subjects.add(Entery2)
print("Unique subjects you entered are: ", subjects)

#Question 3(alternative method)
subjects1 = {
    "Entery" : input("Enter 1st subject: "),
    "Entery1" : input("Enter 2nd subject: "),
    "Entery2" : input("Enter 3rd subject: ")
}
Entery = subjects1["Entery"]
Entery1 = subjects1["Entery1"]  
Entery2 = subjects1["Entery2"]
subjects = set()
print(type(Entery2))
subjects.add(Entery)
subjects.add(Entery1)
subjects.add(Entery2)

print("your subjects are: ", subjects)


#Question 4
'''Figure out a way to store 9 & 9.0 as separate values in the set.
(You can take help of built-in data types)'''
col = {
    ("integer", 9),
    ("float", 9.0)
}
print(col)
print("Number of elements in the set: ", len(col))
#both 9 and 9.0 are considered same in set as they have same hash value