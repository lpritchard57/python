#This program will allow you to evaluate your expenses and compare them to your monthly budget
print("Hello!")
print("")
print("In order for the program to run efficiently, please avoid the usage of commas and monetary symbols in your responses. Thank you!\n")
budg = float(input("Please enter your monthly budget: ")) #The float function does not recognize commas or monetary symbols
print("")
print("Thank you!\nNow enter the amount spent per month for each category:\n")
# The section below represnts the total expenses for each category
hous = (float(input("Housing expenses: ")))
util = (float(input("Utility expenses: ")))
groc = (float(input("Grocery expenses: ")))
tran = (float(input("Transportation expenses: ")))
hlth = (float(input("Healthcare expenses: ")))
pers = (float(input("Personal care expenses: ")))
clot = (float(input("Clothing expenses: ")))
debt = (float(input("Debt expenses: ")))
print("")
# The section below will show the percentage of budget used per each category
print(f"Housing expenses take up {hous/budg*100:.2f} percent of your total budget.")
print(f"Utility expenses take up {util/budg*100:.2f} percent of your total budget.")
print(f"Grocery expenses take up {groc/budg*100:.2f} percent of your total budget.")
print(f"Transportation expenses take up {tran/budg*100:.2f} percent of your total budget.")
print(f"Healthcare expenses take up {hlth/budg*100:.2f} percent of your total budget.")
print(f"Personal care expenses take up {pers/budg*100:.2f} percent of your total budget.")
print(f"Clothing expenses take up {clot/budg*100:.2f} percent of your total budget.")
print(f"Debt expenses take up {debt/budg*100:.2f} percent of your total budget.")
print("")
print("I hope this helped! Have a wonderful day!")