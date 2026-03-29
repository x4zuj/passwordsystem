
# Welcome to my simple password_funtion.py
# This is just a simple login system made by 4zuj.

# First of All, I need variables, else this won't work.

password = "required"
user_input = input("Welcome User, who is logging in?: ") # Just some decoration c:

while password == "required":
    print(user_input,"Enter your password. ")
    password_input = input("Password: ")
    if password_input == "Test123":
        password = "correct"
        print("Successfully in!")
        input("Press ENTER or Ctrl+C to exit the program.")
    else:
        print("The password is incorrect. Please try it again. ")
