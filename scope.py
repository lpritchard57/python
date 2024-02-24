#The following are global variables; will be recognized throughout program
pounds_to_kilograms = float(input("Enter your weight in pounds: "))
inches_to_meters = float(input("Enter your height in inches: "))

#Converts the inputs into the metric system
weight = pounds_to_kilograms*.453592
height = inches_to_meters*.0254

#Calculates the BMI using the metric units 
BMI = weight/(height**2)
print(f"Your BMI is {BMI:,.2f}")

#Will tell user which category they are in based on the BMI calculated
if BMI < 18.5:
    print("You are in the underweight category.")
elif BMI < 24.9:
    print("You are in the normal weight category.")
elif BMI < 29.9:
    print("You are in the overweight category.")
else:
    print("You are in the obese category.")