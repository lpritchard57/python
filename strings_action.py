def main():
    titles = []
    count = 0

    while count < 10:
        title = input("Enter a book title here: ")
        titles.append(title)
        count += 1

    sorted_titles = sorted(titles)

    print("Sorted Book Titles: ")
    for title in sorted_titles:
        print(title)

main()