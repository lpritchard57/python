a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))

if a>20 and b>20:
    print("Both integers are greater than 20: True")
else:
    print("Both integers are greater than 20: False")

if a<=0 and b<=0:
    print("Both numbers are less than or equal to zero: True")
else:
    print("Both numbers are less than or equal to zero: False")

if a%2 == 0 or b%2 == 0:
    print("Either number is divisble by 2: True")
else:
    print("Either number is divisible by 2: False")

if a*10 > 100 or b*10 > 100:
    print("Either number multiplied by 10 is greater than 100: True")
else:
    print("Either number multiplied by 10 is greater than 100: False")

if not a>b:
    print("The first integer is not greater than the second integer: True")
else:
    print("The first integer is not greater than the second integer: False")

if not a*b>100:
    print("Both integers multiplied together are not greater than 100: True")
else:
    print("Both integers multiplied together are not greater than 100: False")