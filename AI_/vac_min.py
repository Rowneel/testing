def vacuum_world():
    environment = {}
    cost = 0
    def clean_location(location):
        nonlocal cost
        if environment[location] == '1':
            print(f"Location {location} is Dirty.")
            environment[location] = '0'
            cost += 1
            print(f"Location {location} has been cleaned.")
            print(f"Cost after cleaning {location}: {cost}")
        else:
            print(f"No Action! Location {location} is already clean.")

    def move_to_location(location):
        nonlocal cost
        if location == 'A':
            print("Moving to Location A.")
        else:
            print("Moving to Location B.")
        cost += 1
        print(f"Cost after moving to {location}: {cost}")

    status_A = input("Enter status of location A: ")
    status_B = input("Enter status of location B: ")
    environment['A'] = status_A
    environment['B'] = status_B
    location = input("Enter location of vacuum cleaner (A or B): ").upper()
    print(f"Initial Environment: {str(environment)}")
    if location == 'A':
        print("Vacuum is placed in Location A")
        clean_location('A')
        move_to_location('B')
        clean_location('B')
    else:
        print("Vacuum is placed in Location B")
        clean_location('B')
        move_to_location('A')
        clean_location('A')
    print(f"Goal State: {str(environment)}")
    print(f"Performance Measure: {cost}")
vacuum_world()