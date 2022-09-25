import os


# For making some bold print
class login:
    bold = '\033[1m'
    end = '\033[0m'


# Clear function depending on operating system
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


# Encryption function
def encrypt(name):
    return " ".join([str(i) for i in [ord(i) + 31874614 % 128 for i in list(name)]])

    # Takes string input
    # Converts string to list
    # Applies some rules for each item in list
    # Converts list of integers to strings and joins with " "
    # Returns


def main():
    while True:  # 'Login loop' for entire login process - allows for restarts
        while True:  # 'While' loop for username input - ensures username is valid and entered twice
            user = input("Please enter a username for a new or existing account: ")
            if len(user) > 8:
                cls()
                print("Username must be 8 characters or less." + '\n')
                continue
            elif not user.isalpha():
                cls()
                print("Username can only contain alphabet." + '\n')
                continue
            elif input("Please confirm your username: ") == user:  # Makes user enter username twice to avoid typos
                break
            else:
                cls()
                print("Usernames did not match." + '\n')
                continue

        user_encrypted = encrypt(user)  # Encrypts username

        with open('user_details', 'a+') as file:
            file.seek(0)  # Seeks to start of file
            new = 1  # keeps track of whether a new account needs to be made - default is 1 (needs new account)
            success = 0  # keeps track of whether login has been successful - default is 0 (not successful yet)
            if file.readlines():  # Checks for empty user_details.txt
                index = -1  # Index variable to later locate the matching password for any existing username
                file.seek(0)
                for i in [line[:line.find(',')] for line in file.readlines()]:  # Loop that checks for username
                    # Retrieves all elements before the comma for each line in the file by using split syntax [:]
                    index += 1  # 'index' = 'index' +1 for every line checked
                    if user_encrypted == i:  # Compares inputted username with usernames on file
                        cls()
                        new = 0  # If match, sets 'new' to 0 (doesn't need new account anymore)
                        file.seek(0)
                        pw_onfile = file.readlines()[index].split(', ')[1][:-1]

                        # Matching password (pw_onfile) is retrieved by:
                        # getting the appropriate username and password string in user_details.txt at line 'index'
                        # splitting the string by ', '
                        # keeping the second item of the split string (the password)
                        # removing '\n' from end of password string

                        pw_encrypted = encrypt(input("Hi " + login.bold + user + login.end +
                                                     ". Please enter your password: "))
                        if pw_encrypted == pw_onfile:  # If inputted password matches password on file...
                            input('\n' + "Login Successful. Hit enter to continue...")
                            success = 1  # Sets 'success' to 1 (login is successful)
                        else:  # If first password attempt isn't correct...
                            count = 2
                            while count > 0:  # Forces another 2 attempts until login restart
                                cls()
                                pw_encrypted = encrypt(input("Incorrect. " + login.bold + str(count) + login.end +
                                                             " attempts remaining. Please try again: "))
                                if pw_encrypted != pw_onfile:
                                    count -= 1
                                    continue
                                else:
                                    input('\n' + "Login Successful. Hit enter to continue...")
                                    success = 1  # Sets 'success' to 1 (login is successful)
                                    break

                            if count == 0:  # If max password attempts has been hit...
                                cls()
                                print("Too many attempts! Back to login..." + '\n')
                                break

                        break  # Breaks loop that checks for username

            if new == 1:  # If 'new' = 1
                cls()
                while True:  # 'While' loop for password input to ensure password is valid and entered twice
                    pw = input("User " + login.bold + user + login.end +
                               " not found. Please enter a password to register: ")
                    cls()
                    if not pw.isdigit():
                        print("Password can only contain numbers." + '\n')
                        continue
                    elif len(pw) > 4:
                        print("Password must be 4 digits or less." + '\n')
                        continue
                    elif input(
                            "Please confirm the password for " + login.bold + user + login.end + ": ") == pw:
                        # Makes user enter password twice to avoid typos
                        pw_encrypted = encrypt(pw)
                        file.write(user_encrypted + ', ' + pw_encrypted + '\n')
                        input(
                            "Thanks user " + login.bold + user + login.end + ". Your password is " +
                            login.bold + pw + login.end + ". Hit enter to continue...")
                        success = 1
                        break  # Breaks 'while' loop when valid and confirmed password
                    else:
                        cls()
                        print("Passwords did not match." + '\n')
                        continue

        if success == 0:  # If 'success' remains as 0: 'Login loop restarts', otherwise breaks
            continue
        else:
            return user


if __name__ == "__main__":
    main()
