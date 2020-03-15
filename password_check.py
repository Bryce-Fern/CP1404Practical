length_password = 4

def main():
    password = get_password()
    while len(password) < length_password:
        password = input("Invalid password, password must have at least {} characters: ".format(length_password))
    else:
        asterisks(password)


def asterisks(password):
    print('*' * len(password))


def get_password():
    password = input("Enter a password with {} or more characters: ".format(length_password))
    return password


main()


