your_age = int(input("How old are you?: ")) #Enter age here

if your_age >= 16:
    print("You are old enough to drive.") 
    if your_age >= 18:
        print("You are old enough vote.") #Ex: Any age entered below 18 will
        #only print the first "if" statement
        if your_age >= 21:
            print("You are old enough to purchase alcohol.")
            if your_age >= 65:
                print("You are eligible for a senior discount.")
else:
    print("You are not old enough for the categories above.") #Any age 
    #entered below 16 will only print the "else" statement