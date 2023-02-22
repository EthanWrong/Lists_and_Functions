def get_car(vehicles):
    try:
        car_num = int(input("Enter car number to book: "))
        if car_num not in vehicles or vehicles[car_num]["booked"]:
            print("That car is not available to be booked")
            return get_car(vehicles)
        else:
            return car_num
    except ValueError:
        print("Please enter a valid number")
        return get_car(vehicles)


def get_name():
    name = input("Enter your name: ")
    return name


def capitalize_name(name):
    if name:
        cap_name = ""
        for i in name.split():
            cap_name += i.capitalize() + " "
        return cap_name.rstrip()
    return None


def get_seats_required():
    try:
        seats_required = int(input("How many seats do you need? (Enter -1 "
                                   "to quit): "))
        return seats_required
    except ValueError:
        print("Please enter a valid number")
        return get_seats_required()


def print_cars(vehicles, seats_required):
    print(f"{'#':<2} {'MODEL':<20}    {'SEATS':<10}")
    for car in vehicles:
        note = "NOTE: Not enough seats" if vehicles[car]["seats"] < \
                                           seats_required else ""
        if not vehicles[car]["booked"]:
            print(f"{car}) {vehicles[car]['model']:<20} - "
                  f"{vehicles[car]['seats']:>2} seats - {note}")


def print_bookings(bookings):
    print("VEHICLES BOOKED TODAY")
    print(f"{'#':<2} {'MODEL':<20}   {'BOOKED BY'}")
    for car in bookings:
        if bookings[car]["booked"]:
            name = capitalize_name(bookings[car]["booked"])
            print(f"{car}) {bookings[car]['model']:<20} - {name}")


def book_car(vehicles):
    seats_required = get_seats_required()
    if seats_required == -1:
        return vehicles
    print_cars(vehicles, seats_required)
    car_num = get_car(vehicles)
    name = get_name()
    vehicles[car_num]["booked"] = name
    print()
    return book_car(vehicles)


def main(vehicles):
    bookings = book_car(vehicles)
    print_bookings(bookings)
    return bookings


VEHICLES = {
    1: {"model": "Suzuki Van", "seats": 2, "booked": False},
    2: {"model": "Toyota Corolla", "seats": 4, "booked": False},
    3: {"model": "Honda CRV", "seats": 4, "booked": False},
    4: {"model": "Suzuki Swift", "seats": 4, "booked": False},
    5: {"model": "Mitsubishi Airtrek", "seats": 4, "booked": False},
    6: {"model": "Nissan DC Ute", "seats": 4, "booked": False},
    7: {"model": "Toyota Previa", "seats": 7, "booked": False},
    8: {"model": "Toyota Hi Ace", "seats": 12, "booked": False},
    9: {"model": "Toyota Hi Ace", "seats": 12, "booked": False},
}


# all vehicles and their states of booked are stored in variable bookings1
bookings1 = main(VEHICLES)
