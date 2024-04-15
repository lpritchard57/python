class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message

def main():
    while True:
        try:
            user_input = input("Enter a number: ")
            number = float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue  
        else:
            print("You entered a valid number:", number)
            break  
        finally:
            print("End of program.")

main()



