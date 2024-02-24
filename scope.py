pounds_to_kilograms = float(input("Enter your weight in pounds: "))
inches_to_meters = float(input("Enter your height in inches: "))

weight = pounds_to_kilograms*.453592
height = inches_to_meters*.0254

BMI = weight/(height**2)
print(f"Your BMI is {BMI:,.2f}")

if BMI < 18.5:
    print("You are in the underweight category.")
elif BMI < 24.9:
    print("You are in the normal weight category.")
elif BMI < 29.9:
    print("You are in the overweight category.")
else:
    print("You are in the obese category.")