print("\n----ACTIVITIES FOR THE FIRST SEMESTER----")
name = input("ENTER YOUR NAME:")

def activity1():
    print("\nHello World")
    print("Hello my Fellow Programmer")

def activity2():
    age = input("\nEnter your age:")
    email = input("Enter your email:")
    
    print("\nHi!" + name + " ,welcome to coding world!\n"+ "Your current age is " + age + " years old\n"+ "and your email address is " + email)
    
    print("\nYour name consists of ", len(name), " letters")
    
    num1 = eval(input("\nEnter a number:"))
    num2 = eval(input("Enter another number:"))
    
    print(num1 , "+" , num2, "=", num1 + num2 )

def activity3():
    age = input("\nEnter your age: ")
    address = input("Enter your address: ")
    
    print(f"\nHi {name}, from {address} and currently {age} years old")

def activity4():
    f = eval(input("\nEnter the Fahrenheit to convert:"))
    c = (f - 32) * 5 / 9
    
    print(f"\n{f} degree Fahrenheit converted to Celsius is {round(c, 2)}")
    cel = eval(input("\nEnter the Celsius:"))
    
    fah = (cel * 9 / 5) + 32
    
    print(f"\n{cel} degree Celsius converted to Fahrenheit is {round(fah, 2)}")

def activity5():
    x = 10
    print(x)
    
    x += x+10
    print(x)
    
    x += x+10
    print(x)
    
    x *= 10
    print(x)
    
    x -= 600
    print(x)
    
    x /= 10
    print(x)

def activity6():
    password = "helloworld"

    mypassword = input("\nEnter Password:")
    if password == mypassword.lower():
        print("Welcome to the world of programmers")
    
    elif mypassword.lower() == "python":
        print("Welcome, Programmer")
    
    else:
        print("Access Denied, Try Again")
    
def activity7():
    isEnrolled = input("\nAre your enrolled in DLL(yes/no):")
    
    if isEnrolled.lower() == "yes":
        print(f"Hi {name}, welcome to DLL scholarship application")
        
        age = eval(input("Enter your age:"))
        
        if age >= 18 and age<= 35:
            print("Your age is qualified with the age requirement")
            
            is4ps = input("Are you a 4ps beneficiary?(yes/no)")
            if is4ps.lower() == "yes":
                
                print("Congratualations! Your are now a certified Scholar ng bayan ")
            
            else:
                print("Sorry for 4ps benificiaries only")
        else:
            print("Your age doesn't meet the age requirements")
    else:
        print("Sorry not applicable for non-dalubhacenian") 

def activity8():
    sum = 0
    odd = 0
    even = 0
    
    for x in range(1,11):
        num = eval(input(f"\nInput Number {x}:"))
        sum += num
        
        if num % 2 == 0:
            even += num
            
        else:
            odd += num
            
    print(f"\nThe sum of all numbers are: {sum}")
    print(f"The sum of all even numbers are: {even}")
    print(f"The sum of all odd numbers are: {odd}")

def activity9():
    num = eval(input("\nEnter any number:"))
    factorial = 1
    
    for x in range(num,0, -1):
        factorial *= x
        
    print(f"\nThe Factorial of {num} is {factorial}")

def activity10():
    for x in range (1,11):
        print(x, end=" ")
        for y in range (1,11):
            print("*", end= " ")
        print()

def activity11():
    for x in range (1,11):
        for y in range (1,x+1):
            print(" ", end= " ")
        for z in range (11, x,-1):
            print("*", end=" ")
        print()


while True:
    print("\nOPTIONS:")
    print("1 -- ACTIVITY 1")
    print("2 -- ACTIVITY 2")
    print("3 -- ACTIVITY 3")
    print("4 -- ACTIVITY 4")
    print("5 -- ACTIVITY 5")
    print("6 -- ACTIVITY 6")
    print("7 -- ACTIVITY 7")
    print("8 -- ACTIVITY 8")
    print("9 -- ACTIVITY 9")
    print("10 -- ACTIVITY 10")
    print("11 -- ACTIVITY 11")
    print("12 -- EXIT")
    
    
    choice = input("\nCHOOSE AN OPTION: ")
    
    if choice == '1':
        activity1()
    elif choice == '2':
        activity2()
    elif choice == '3':
        activity3()
    elif choice == '4':
        activity4()
    elif choice == '5':
        activity5()
    elif choice == '6':
        activity6()
    elif choice == '7':
        activity7()
    elif choice == '8':
        activity8()
    elif choice == '9':
        activity9()
    elif choice == '10':
        activity10()
    elif choice == '11':
        activity11()
    elif choice == '12':
        print("\nTHANK YOU FOR USING MY CODES")
        print("EXITING...")
        break
    else:
        print("INVALID OPTION, PLEASE TRY AGAIN")
