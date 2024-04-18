#this is a generator function that prints every possible two letter combination from a list of characters
def two_letter_combinations(characters):

    for char1 in characters: #will iterate through the list of characters
        for char2 in characters:
            yield char1 + char2 #will concatenate the two characetrs and give an input to the code for each iteration

def main():
    characters = ['l','m','n','o','p']

    combinations_generator = two_letter_combinations(characters) #calls the generator function and the list of characters

    for combination in combinations_generator: #will iterate through the generator and provide every possible combination of characters
        print(combination)

main()