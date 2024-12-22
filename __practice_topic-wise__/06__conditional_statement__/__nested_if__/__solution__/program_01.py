#Write a program to create an Instagram login page.
'''
    - Input Required:
        - Username (`input()`): Ask the user to enter their Instagram username.
        - Password (`input()`): Ask the user to enter their password.
    - Check if the entered username exists in the database (simulate with predefined values).
        - If the username is valid, check the password.
        - If the password matches:
            - Print a success message: "Login successful! Welcome to Instagram."
        - Else: Print: "Incorrect password. Please try again."
    - If the username is invalid, print: "Username not found. Please sign up."
    - Extra Features:
        - Add a "Forgot Password?" option to simulate a password recovery process.
        - Allow three attempts for login before locking the account.
'''

username = input("Enter the username:")


usr = "ichigo_kurosaki"
pas = "ichigo@kurosaki"


if username == usr :
    print(f"Hello, {usr} welcome!")

    password = input("Now Enter your password: ")
    
    if password == pas:
        print("Login successfull! Welcome to Instagram.")

    elif password != pas:
        print("You have a entered Incorrect Password!!")
        select= input("Want to Reset Password? Yes or No: ")

        if select== "Yes":
            print("Check you Mail-ID for Reset link.")
        
        else:
            print("Thank you for visiting.")

else:
    print("Username not found. Please sign up.")





