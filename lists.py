days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
steps = []


for i in days:
    number_of_steps = input(f"How many steps did you take on {i}?: ")
    steps.append(int(number_of_steps))

for i in range(len(days)):
    print(f"You took {steps[i]} steps on {days[i]}.")

total_steps = sum(steps)
print("\nTotal steps:", total_steps)

average = round(total_steps/len(steps))
print("Average steps:", average)
