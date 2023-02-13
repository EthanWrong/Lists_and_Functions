def main(roll):
    while True:
        print("Please select a task:\n"
              "1 Drop off a Child\n"
              "2 Pick up a child\n"
              "3 Calculate cost\n"
              "4 Print roll\n"
              "x Exit")
        choice = input("> ").lower()
        if choice == "1":
            drop_off(roll)
        elif choice == "2":
            pick_up(roll)
        elif choice == "3":
            calc_cost(roll)
        elif choice == "4":
            print_roll(roll)
        elif choice in ("5", "x"):
            break
        else:
            print(f"{choice} is not a valid task.")
        print()

    return roll


def drop_off(roll):
    child = input("What is the child's name?\n"
                  "> ").lower()
    if child in roll:
        print(f"There is already a {child.capitalize()} in this roll.\n"
              f"Please add a surname, or 'x' to exit to main menu")
        return drop_off(roll)
    elif child == "x":
        return roll
    else:
        roll.append(child)
        print(f"{child.capitalize()} has been added to the roll")

    return roll


def pick_up(roll):
    child = input("What is the child's name?\n"
                  "> ").lower()
    if child in roll:
        roll.remove(child)
        print(f"{child.capitalize()} has been removed from the roll")
    elif child == "x":
        return roll
    else:
        print(f"There is no {child.capitalize()} in the roll.\n"
              f"You may want to print roll if you have forgotten their name.\n"
              f"Enter 'x' to exit to main menu.")
        return pick_up(roll)

    return roll


def calc_cost(roll):
    try:
        hours = int(input("For how many hours?\n"
                          "> "))
    except ValueError:
        print("Invalid, input, please enter an integer")
        return calc_cost(roll)

    kids = len(roll)
    cost = COST_PER_HOUR * kids * hours
    print(f"Total cost for looking after\n"
          f"{kids} kids for\n"
          f"{hours} hours at\n"
          f"${COST_PER_HOUR} an hour is:\n"
          f" ${cost}")

    # allows user to see results
    input("Enter to continue\n"
          "> ")
    return


def print_roll(roll):
    print("Current children on the roll")
    for num, child in enumerate(roll):
        print(f" {num+1} {child.capitalize()}")

    # allows user to see results
    input("Enter to continue\n"
          "> ")


# main routine

COST_PER_HOUR = 12
mgs_roll = []

welcome_msg = "Welcome to MGS Childcare"
print("*"*len(welcome_msg))
print(welcome_msg)
print("*"*len(welcome_msg))


mgs_roll = main(mgs_roll)
print("Your roll is saved into the variable 'mgs_roll'.\n"
      "Goodbye!")