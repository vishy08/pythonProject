
pwd = input("what is the master password? ")

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip())

def add():
    name = input("Account Name: ")
    password = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + password + "\n")

while True:
    mode = input("would you like to add a new password or view existing ones? (view/add)")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode")
        continue