#Q1_checking username and password

username = input("Username: ")
password = input("Password: ")

if username == 'admin':
    if password == 'admin':
        print('Welcome!')
    else:
        print("Wrong Data")
else:
    print("Hello",username)


