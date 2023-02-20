def get_num(msg):
    try:
        return float(input(msg))
    except ValueError:
        print("Please enter a valid number")
        return get_num(msg)


def calc_income(minutes):
    return round(10 + minutes*2, 2)


def new_trip(trips):
    choice = input("Start a new trip: (y/n)").lower()
    if choice in ("yes", "y"):
        minutes = get_num("Time of trip in minutes: ")
        trips.append(minutes)
        print(f"Cost of trip: ${calc_income(minutes)}")
        return new_trip(trips)
    elif choice in ("no", "n"):
        return trips
    else:
        print("Invalid choice. Please enter 'y' or 'n'")
        return new_trip(trips)


def get_avg_time(trips):
    count = 0
    total = 0
    for i in trips:
        count += 1
        total += i
    return round(total/count, 2)


def get_avg_cost(trips):
    count = 0
    total = 0
    for i in trips:
        count += 1
        total += calc_income(i)
    return round(total/count, 2)


def get_total_income(trips):
    income = 0
    for i in trips:
        income += calc_income(i)
    return income


def get_total_time(trips):
    time = 0
    for i in trips:
        time += i
    return time


name1 = input("Name: ")
trips1 = new_trip([])
print()
print(f"{name1.capitalize()}")
print(f"Total time: {get_total_time(trips1):.2f} min")
print(f"Total cost: ${get_total_income(trips1):.2f}")
print(f"Average time: {get_avg_time(trips1)} min")
print(f"Average cost: ${get_avg_cost(trips1)}")
