#Create account command
def create_account():
    main = True
    while main:
        username = input("Enter your username: ")
        while True:
            password = input("Enter your password: ")
            confirmation = input("Confirm your password: ")
            if password == confirmation:
                print()
                break
            else:
                print("Password did not match, please try again.")
                print()
                continue

        print("Username:", username)
        print("Password:", password)
        while True:
            correct = input("Is this correct? (Y/N): ").upper()
            if correct == "YES" or correct == "Y":
                main = False
                break
            elif correct == "NO" or correct == "N":
                break
            else:
                continue
    return username, password


#Recreate password command
def recreate_password(old_password):
    password_creation = True
    print(f"Your old password is: {old_password}")
    while password_creation:
        while True:
            password = input("Enter your new password: ")
            pass_confirm = input("Confirm your new password: ")
            if password == pass_confirm:
                print()
                print("Your new password is: ", password)
                break
            else:
                print("Password did not match, please try again.")
                print()
        while True:
            correct = input("Is this correct? (Y/N): ").upper()
            if correct == "YES" or correct == "Y":
                password_creation = False
                break
            elif correct == "NO" or correct == "N":
                break
            else:
                print("Invalid Input.")
    return password


#Show information command
def show_info(username, password):
    print(f"Your username is: {username}")
    print(f"Your password is: {password}")


#Delete account command
def delete_account(username, password):
    while True:
        validation = input("Are you sure you want to delete your account? (Y/N): ").upper()
        if validation == "YES" or validation == "Y":
            username = ""
            password = ""
            print("Your account has been deleted.")
            return username, password
            break
        elif validation == "NO" or validation == "N":
            break
        else:
            print("Invalid Input.")
            continue


#Main Script
username = ""
password = ""
print('''Welcome, you can create and manage your account here.
If you want to see the list of commands type 'help'.''')
while True:
    print()
    command = input("Enter command: ").lower()
    if command == "exit":
        input("Press enter to exit...")
        break
    elif command == "help" or command == "h":
        print('''1. Create Account
2. Recreate Password
3. Show Info
4. Delete Account
5. Exit''')

    elif command == "create account":
        username, password = create_account()
    elif command == "recreate password":
        if username != "" and password != "":
            password = recreate_password(password)
        else:
            print("No account has been made.")          
    elif command == "show info" or command == "show":
        if username != "" and password != "":
            show_info(username, password)
        else:
            print("No account has been made.") 
    elif command == "delete account":
        if username != "" and password != "":
            try:
                username, password = delete_account(username, password)
            except:
                continue
        else:
            print("No account has been made.") 
    else:
        print("Invalid Input.")