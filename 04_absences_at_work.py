def yes_no(msg):
    choice = input(msg).lower()
    if choice in ("yes", "y"):
        return True
    elif choice in ("no", "n"):
        return False
    else:
        return yes_no(msg)


def get_input():
    user = input("Enter <name> <absences>: ")

    # to terminate input
    if user == "$":
        return None, None
    elif user == "":
        return get_input()

    user_words = user.split()
    name, absences = "", 0

    for i in user_words:
        try:
            i = int(i)
            absences = i
        except ValueError:
            name += i.capitalize() + " "

    name = name.rstrip().strip(",")
    return name, absences


def add_entry(roll):
    name, absences = get_input()
    done = False

    # input has been terminated
    if not name:
        done = True

    # name has already been added
    elif name in roll.keys():
        print("<err> Name has already been added")
    # add name to roll
    else:
        roll[name] = absences
        print(f"Added: {name}; {absences}")

    return roll, done


def print_results(roll):
    print()
    names = list(roll.keys())

    width = 0
    for i in names:
        if len(i) > width:
            width = len(i)

    print(f"{'Name':<{width}}   Absences")
    for i in roll:
        print(f"{i:<{width}} : {roll[i]}")
    print()

    # find avg days absent
    total, count = 0, 0
    for i in roll:
        total += roll[i]
        count += 1
    avg_days_absent = round(total/count, 2)
    print(f"{'Avg days absent:':<29} {avg_days_absent}")

    # find person with most absences
    most_absent_people = []
    days_absent = 0
    for i in roll:
        if roll[i] > days_absent:
            days_absent = roll[i]
            most_absent_people.clear()
            most_absent_people.append(i)
        elif roll[i] == days_absent:
            most_absent_people.append(i)
    print(f"{'Most days absent:':<25} {days_absent:>2}; "
          f"{most_absent_people[0]}")
    for i in most_absent_people[1:]:
        print(f"{30*' '}{i}")

    # find people without any absences
    no_absences = []
    for i in roll:
        if roll[i] == 0:
            no_absences.append(i)
    if no_absences:
        print(f"{'People not absent at all:':<30}"
              f"{no_absences[0]}")
        for i in no_absences[1:]:
            print(f"{30 * ' '}{i}")
    else:
        print("No people were not absent at all")

    # find people absent above average
    above_average = []
    for i in roll:
        if roll[i] > avg_days_absent:
            above_average.append(i)
    if above_average:
        print(f"{'People absent above avg:':<30}"
              f"{above_average[0]:<20}; {roll[above_average[0]]}")
        for i in above_average[1:]:
            print(f"{30 * ' '}{i:<20}; {roll[i]}")
    else:
        print("No people were absent above avg")


def main(roll):
    print("Welcome to *Absences at Work*")
    print("Simply enter the name of the person (may be first, last, "
          "and any middle names separated by spaces),")
    print(" followed by the number of days they were absent. Blank will be "
          "assumed as 0")
    print("Enter '$' to terminate entry")
    print()
    while True:
        roll, done = add_entry(roll)
        if done:
            break
    print_results(roll)

    return roll


workplace_roll = {}

# to save roll in a variable for later use
workplace_roll = main(workplace_roll)

