import random

def main():
    try:
        target_number = random.randint(1,100)
        guess = -1

        while guess != target_number:
            guess = int(input("Enter a number between 1 and 100: "))
            difference = abs(guess - target_number)

            if guess < 1 or guess > 100:
                print("Number entered is not in range.")
                main()
            if difference <= 5:
                print("Very hot.")
            elif difference <= 15:
                print("Hot.")
            elif difference <= 25:
                print("Cool.")
            else:
                print("Cold.")
        print("You guessed the correct number!")

    except ValueError:
        print("Please enter a valid integer.")
        main()

main()