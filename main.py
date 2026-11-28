users = []

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        password = input("Enter password: ")
        users = users + [[name, password]]
        print("Registration successful!")

    elif choice == "2":
        name = input("Enter name: ")
        password = input("Enter password: ")
        
        login_ok = False
        for u in users:
            if u[0] == name and u[1] == password:
                print("Login successful!")
                print("Welcome", name)
                login_ok = True

        if login_ok == False:
            print("Invalid name or password!")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")