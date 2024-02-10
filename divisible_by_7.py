for number in range(1,300): # this gives a range of numbers for the program 
    # to process
    if number %7 == 0: # if number is divisible by 7, it will print
        print(number)
    else: 
        continue # if number is not divisible by 7, the program will skip 
        # until another number within range is divisible by 7