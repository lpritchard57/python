def main():
    #prompts user to enter date and time as well as their diary entry
    date_and_time = input("Enter the current date and time (format = xx/xx/xxxx at xx:xx AM/PM): ")
    entry = input("Write your entry here: ")

    with open("diary.txt", 'a') as diary_file: #opens existing or creates new file named diary.txt
        #each entry is added to the diary.txt file and is separated with a blank line using ("\n")
        diary_file.write(date_and_time + "\n")
        diary_file.write(entry + "\n")
        diary_file.write("\n")

    diary_file.close() #file is closed and entries are saved 

main()