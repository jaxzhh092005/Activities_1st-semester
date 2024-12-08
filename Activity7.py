name= input("Enter your name:")

isEnrolled = input("Are your enrolled in DLL(yes/no):")

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