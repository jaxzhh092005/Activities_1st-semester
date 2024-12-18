a= True
tri = 0
while a== True :
    b= input("Do you wish to print more triangles (yes/no)?")

    if b.lower()== "no":
        print("LOOP HAS ENDED")
        break
        a = False

    elif b. lower()=="yes":
        tri +=1
        for x in range(1,6):
            for y in range(1, tri + 1):
                for c in range (1, x + 1):
                    print("*", end=" ")
                for d in range (6,x,-1):
                    print (" ", end=" ")
                print(end=" ")
            print()

    else:
        print("INVALID SELCTION")
        print("PLEASE TYPE (YES/ NO)")
        continue