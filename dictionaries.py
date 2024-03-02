def main():
    nato_alphabet = {"A":"Alpha", "B":"Bravo", "C":"Charlie","D":"Delta", 
                   "E":"Echo", "F":"Foxtrot", "G":"Golf", "H":"Hotel", 
                   "I":"India", "J":"Juliette", "K":"Kilo", "L":"Lima", 
                   "M":"Mike", "N":"November", "O":"Oscar", "P":"Papa", 
                   "Q":"Quebec", "R":"Romeo", "S":"Sierra", "T":"Tango", 
                   "U":"Uniform", "V":"Victor", "W":"Whiskey", 
                   "X":"X-Ray", "Y":"Yankee", "Z":"Zulu"}
    user_word = input("Enter a word: ")
    
    for letter in user_word.upper():
        if letter in nato_alphabet:
            print(nato_alphabet[letter])
        else:
            print(f"No NATO phonetic term found for {letter}")
main()