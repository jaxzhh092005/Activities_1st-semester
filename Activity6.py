#decision structures/conditional statements

password = "helloworld"

mypassword = input("Enter Password:")

if password == mypassword.lower():
    print("Welcome to the world of programmers")

elif mypassword.lower() == "python":
    print("Welcome, Programmer")

else:
    print("Access Denied, Try Again")