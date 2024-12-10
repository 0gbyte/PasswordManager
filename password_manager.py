import pm_func as pm
    
if __name__ == "__main__":
    ##Login 
    file = "passwords.txt"

    if pm.login() == 1:
        pass
    else:
        print("Login failed")
        exit(1)

    pm.print_menu()

    while True:
        choice = int(input("Please enter your choice: "))
        if choice < 1 or choice > 4:
            print("Not a vailable option")
        elif choice == 1:
            username = str(input("Enter username: "))
            password = str(input("Enter password: "))
            pm.add_password(file, username, password)
        elif choice == 2:
            pm.list_passwords(file)
        elif choice == 3:
            line = int(input("Enter index of a line to remove: "))
            pm.remove_password(file, line)
        elif choice == 4:
            print("Bye!")
            exit(1)
        pm.print_menu()



