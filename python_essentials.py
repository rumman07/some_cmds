#!/usr/bin/python3.8

users = []
users.append("john")
users.append("linda")
users.append("marry")
users.append("aaron")
users.append("blake")
num = "123"
#Writing for loop in python. : means start of a code block
for u in users:
    print("Username is",u.title())

#Loop for a specific number of a time usinge range
for i in range(1,10):
    print(i)

#Looping through a list usinge range
for i in range(0, len(users)):
    print(users[i])

#Using slicing for Lists
#Slice the 1 and last from List
print(users[1:3])

#Printing slicing output with for loop
for u in users[0:3]:
    print(u)

print("\n")
#This is slicing using the len method to determine the value of the last index
print(len(users))
for u in users[2:len(users) -1]:
    print(u)

#Slicing print every item in the list starting from index one to the append
print(users[1:])
#Slicing print every item in the list starting from index one to the one before the last item in the list
print(users[1:-1])
##Slicing print every item in the list upto the third item in the list
print(users[:3])

#List comprehension - longer version
for i in range(0,len(users)):
    users[i] = users[i] + num
print(users)
print("\n")
#Using list comprehension
users = [u + num for u in users]
print(users)

#Using the join method to join the list of characters in a starting
message = "Hello World!"
print('*'.join(message))

#If conditions
username = "jdoe"
password = "pass123"

if username == "jdoe" and password == "pass123":
    print("Welcome",username)
else:
    print("Sorry, wrong username or password")

#Check if the item given is in the list or not
usernames = ["jdoe","linda","roger","peter"]

if "jdoe" in usernames:
    print('jdoe found')
else:
    print('no username found')

# Using if statement inside a for loop
for e in usernames:
    if e.lower() == "roger":
        print("roger found")
        break

#Using not before in negates the condition in an if statement
info_log = "Please restart the apache daemon"
if "nginx" not in info_log:
    print("nginx not found")

#Tuples are like list but they are immutable i.e they cannot be changed through program execution
#To create a tuple use () instead of [] used to create a list
#Creating and accessing a tuple
priv = ("user","admin")

for p in priv:
    print(p)

#Dictionaries, in python are like a list but it accepts key value pairs, more like a hash in ruby
#Creating and accessing a dictionary
#Contrast - list is created like user = ["jdoe","31","DevOps Engineer","US"]
user = {
    "username":"jdoe",
    "age":"31",
    "job":"DevOps Engineer",
    "country":"US"
}

print("The username is",user["username"],"he is",user["age"],"years old","he works as",user["job"],"and lives in",user["country"])

#Adding dictionaries to List
users = [{"uname":"linda","job":"operator"},{"uname":"peter","job":"sysadmin"},{"uname":"roger","job":"devops"}]
#Accessing the dictionary in the List
for u in users:
    print("Username is",u["uname"],"and job is",u["job"])

#Changing the value of an item in a dictionary
user_details = {"uname":"linda","job":"operator"}
user_details["job"] = "tester"
print(user_details)

#Adding a new item in the dictionary
user_details["password"] = "pass123"
print(user_details)

#Adding a default password item in list of a dictionary
password = "pass123"

for k in range(0,len(users)):
    users[k]["password"] = password

print(users)

#Removing an item i.e. key value pair in a dictionary using the del function
for k in range(0,len(users)):
     del(users[k]["password"])

print(users)

#Looping through a dictionary
langs = {
    "en":"English",
    "es":"Spanish",
    "ar":"Arabic",
    "it":"Italian",
    "ba":"Bangla"
}

for k,v in langs.items():
    print(v,":",k)
