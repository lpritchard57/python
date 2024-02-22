def calculate_interest(principle,rate,time):
    total = (principle*rate*time) / 100
    return total

input_principle = int(input("Enter the principle amount: "))
input_rate = int(input("Enter the interest rate as a whole number"
                        "(5% would be 5): "))
input_time = int(input("Enter the investment time in whole years: "))

interest = calculate_interest(input_principle,input_rate,input_time)

print(f"The simple interest for a principle amount of ${input_principle:,.2f}"
     f" at an interest rate of {input_rate:,.2f}% over a period of"
      f" {input_time} years is: ${interest:,.2f}")