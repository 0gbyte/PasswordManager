import hashlib

def hash(password):
    return hashlib.md5(password.encode()).hexdigest()

def line_index(file):
    passwords_file = open(file, 'r')
    lines = passwords_file.readlines()
    passwords_file.close()
    return len(lines)
        

def login():
    passsword_hash = "caff9d47f432b83739e6395e2757c863"
    for i in range(3):
        login = str(input("Enter username: "))
        password = str(input("Enter password: "))
        if  hash(password) == passsword_hash and login == "admin":
            return 1
        print(f"Wrong username or password")
    
    return 0

def add_password(file, username, password):
    i = str(line_index(file))
    string_to_save = i + " " + username + ":" + password + "\n"
    passwords_file = open(file, "a")
    passwords_file.write(string_to_save)
    passwords_file.close()
    return 0

def list_passwords(file):

    passwords_file = open(file, "r")
    print(passwords_file.read())
    passwords_file.close()

    return 0


def line_index_correction(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()

    f = open(file, 'w')
    for index, line in enumerate(lines):
        if len(line) > 1:
            f.write(str(index) + " " + line.strip().split(" ")[1] + "\n")
    f.close()
    return 0

def remove_password(file, line_to_remove):
    passwords_file = open(file, 'r')
    lines = passwords_file.readlines()
    passwords_file.close()

    passwords_file = open(file, "w")
    for index, line in enumerate(lines):
        if index != line_to_remove:
            passwords_file.write(line)
    passwords_file.close()

    line_index_correction(file)

    return 0


def print_menu():

    print("Welcome to PM:")
    print("1. Add password")
    print("2. List passwords")
    print("3. Remove password")
    print("4. Exit")
