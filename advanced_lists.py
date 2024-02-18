time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
heart_rates = []

for time in time_slots:
    rate = int(input(f"Enter your heart rate for {time}: "))
    heart_rates.append([time,rate])

print(heart_rates)

total = 0
for rate in heart_rates:
    total += rate[1]

average = round(total/len(heart_rates))
print("Your average heart rate today is", average,".")