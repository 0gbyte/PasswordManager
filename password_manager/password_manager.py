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
    pm.open_application(file)


