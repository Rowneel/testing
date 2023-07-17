def vacuum_world():
    environment = {}
    cost = 0
    status_A = input("Enter status of location A: ")
    status_B = input("Enter status of location B: ")
    environment['A'] =  status_A
    environment['B'] =  status_B
    location = input("Enter location of vacuum cleaner (A or B): ").upper()
    print(f"Initial Environment: {str(environment)}")
    
    if location == 'A':
        print("vacuum is placed in Location A")
        if status_A == '1':
            print("Location A is Dirty.")
            environment['A'] = '0'
            cost += 1
            print("Location A has been cleaned.")
            print(f"Cost after cleaning A: {cost}")
            if status_B == '1':
                print("Moving to Location B.")
                print("Location B is Dirty.")
                cost += 1
                print(f"Cost after moving to B: {cost}")
                environment['B'] = '0'
                cost += 1
                print("Location B has been cleaned.")
                print(f"Cost after cleaning B: {cost}")
            else:
                print("Moving to Location B.")
                print("No Action! Location B is already clean")
                cost += 1
                print(f"Cost after moving to B: {cost}")
        if status_A == '0':
            print("No Action! Location A is already clean.")
            if status_B == '1':
                print("Moving to Location B.")
                print("Location B is Dirty.")
                cost += 1
                print(f"Cost after moving to B: {cost}")
                environment['B'] = '0'
                cost += 1
                print("Location B has been cleaned.")
                print(f"Cost after cleaning B: {cost}")
            else:
                print("Moving to Location B.")
                print("No Action! Location B is already clean")
                cost += 1
                print(f"Cost after moving to B: {cost}")  
    else:
        print("vacuum is placed in Location B")
        if status_B == '1':
            print("Location B is Dirty.")
            environment['B'] = '0'
            cost += 1
            print("Location B has been cleaned.")
            print(f"Cost after cleaning B: {cost}")
            
            if status_A == '1':
                print("Moving to Location A.")
                print("Location A is Dirty.")
                cost += 1
                print(f"Cost after moving to A: {cost}")
                environment['A'] = '0'
                cost += 1
                print("Location A has been cleaned.")
                print(f"Cost after cleaning A: {cost}")
            else:
                print("Moving to Location A.")
                cost += 1
                print("No Action! Location A is already clean")
                print(f"Cost after moving to A: {cost}")
        if status_B == '0':
            print("No Action! Location B is already clean.")
            if status_A == '1':
                print("Moving to Location A.")
                print("Location A is Dirty.")
                cost += 1
                print(f"Cost after moving to A: {cost}")
                environment['A'] = '0'
                cost += 1
                print(f"Location A has been cleaned.")
                print(f"Cost after cleaning A: {cost}")
            else:
                print("Moving to Location A.")
                cost += 1
                print("No Action! Location A is already clean")
                print(f"Cost after moving to A: {cost}")    

   
    print(f"Goal State: {str(environment)}")    
    print(f"Performance Measure: {cost}")
    
vacuum_world()