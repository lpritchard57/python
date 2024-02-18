open_seats = list(range(1, 21))

while open_seats:
    for seat in open_seats:
        print(seat)
    taken_seat = input("Please select a seat number (or '0' to finish): ")
    
    if taken_seat == "0":
        break

    taken_seat = int(taken_seat)

    if taken_seat < 1 or taken_seat > 20:
        print("Seat", taken_seat, "is invalid. Please choose another seat.")
    elif taken_seat in open_seats:
        open_seats.remove(taken_seat)
        print("You have selected seat", taken_seat,".")
    else:
        print("Seat", taken_seat, "is already taken. Please choose another seat.")

print("All seats are taken or you've finished choosing your seats.")