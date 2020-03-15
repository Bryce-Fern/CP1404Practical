length_password = 4

password = input("Enter a password with {} or more characters: ".format(length_password))
while len(password) < length_password:
    password = input("Invalid password, password must have at least {} characters: ".format(length_password))
else:
    print('*' * len(password))