def main():
    try:
        with open("sales_totals.txt", 'r') as file:
            total = 0.0
            count = 0

            for line in file:
                try:
                    sales_amount = float(line.strip())
                    total += sales_amount
                    count += 1

                    print("Sales amount:", format(sales_amount, ',.2f'))
                except ValueError:
                    print("Error: Invalid data in file")

        if count > 0:
            average = total/count
        else:
            average = 0.0

        print("Total:", format(total, ',.2f'))
        print("Number of Entries:", count)
        print("Average:", format(average, ',.2f'))

    except FileNotFoundError:
        print("Error: File not found")

main()