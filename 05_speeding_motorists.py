def get_name():
    name = input("Enter name of speeder: ").lower()
    if name in PEOPLE_TO_ARREST:
        print(f"{name.upper()} - WARRANT TO ARREST")

    if name == "":
        return get_name()

    # terminate input stage
    if name == "$":
        return None
    return name


def get_speed():
    try:
        speed = int(input("Enter amount over speed limit: "))
    except ValueError:
        print("Please enter a valid number")
        return get_speed()
    return speed


def calc_fine(speed):
    if speed <= 0:
        return 0
    elif speed < 10:
        return 30
    elif speed <= 14:
        return 80
    elif speed <= 19:
        return 120
    elif speed <= 24:
        return 170
    elif speed <= 29:
        return 230
    elif speed <= 34:
        return 300
    elif speed <= 39:
        return 400
    elif speed <= 44:
        return 510
    else:
        return 630


def capitalize_name(name):
    if name:
        cap_name = ""
        for i in name.split():
            cap_name += i.capitalize() + " "
        return cap_name.rstrip()
    return None


def get_entry():
    print("#" * 10)
    name = capitalize_name(get_name())

    # if input stage is terminated
    if not name:
        speed, fine = None, None
        return name, speed, fine

    speed = get_speed()
    fine = calc_fine(speed)
    print(f"{name} to be fined ${fine:.0f}")
    return name, speed, fine


def main():
    data = {}

    print("## Welcome to Speeding Motorists ##")
    print("Enter '$' at any time to terminate input stage.")
    print()

    while True:
        name, speed, fine = get_entry()
        if name:
            data[name] = {}
            data[name]["speed"], data[name]["fine"] = speed, fine
        else:
            break

    # display stats
    num_of_fines = len(list(data.keys()))
    total_fines = 0

    print("#"*10)
    print(f"Number of fines today: {num_of_fines}")
    for count, val in enumerate(data):
        _name = list(data.keys())[count]
        _speed = data[val]["speed"]
        _fine = data[val]["fine"]
        print(f"{count+1}) Name: {_name:<15} - Amount Over Limit: {_speed}")
        total_fines += _fine
    print(f"Total amount of fines: ${total_fines}")

    # return to be stored in variable
    return data


PEOPLE_TO_ARREST = ("james wilson", "helga norman", "zachary conroy")

day1_fines = main()
