names = []
swapped = True
name = int(input("Enter the number of names you want to sort: "))

for i in range(name):
    enter_name = input("Enter a name: ")
    enter_name = enter_name.lower()
    names.append(enter_name)

while swapped:
    swapped = False
    for i in range(len(names) - 1):
        if names[i] > names[i+1]:
            swapped = True
            names[i], names[i+1] = names[i+1], names[i]

print("\nSorted: ")
print(names)
print("Reversed:")
names.reverse()
print(names)
