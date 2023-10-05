#just import, I need to do stuff like contact.<function name>
from Functions import *
import os

if __name__=="__main__":
    with open("users.json") as f:
        users = json.load(f)

    user_status = input("Choose the operation you want:\n1. Log in\n2. Sign up\n")
    login_status = False
    user_id = "default"

    if user_status == "1":
        user_id = input("ID: ")
        user_existance = False

        for user in users["data"].keys():
            if user == user_id:
                user_existance = True
                break

        if user_existance == False:
            raise ValueError("Your ID does not exist. Or you've entered an invalid ID")

        user_password = input("Password: ")

        if user_password == users["data"][user_id]["Password"]:
            login_status = True

        else:
            raise ValueError("Your Password is incorrect. Get TF out.")

    elif user_status == "2":
        print("We're signing you up. Please fill out your information.")
        user_PN = input("Enter Phone Number: ")
        user_FN = input("Enter First Name: ")
        user_LN = input("Enter Last Name: ")
        user_id = input("Enter ID: ")
        user_password = input("Enter Password: ")
        user_password_check = input("Confirm Password: ")

        while user_password != user_password_check:
            print("Password Confirm failure")
            user_password = input("Enter Password: ")
            user_password_check = input("Confirm Password: ")

        with open('users.json') as infile:
            users = json.load(infile)
        
        new_user = {user_id:{"Password":user_password, "FirstName": user_FN, "LastName": user_LN, "Phonenum": user_PN}}
        users["data"].update(new_user)
        
        with open('users.json', "w") as outfile:
            json.dump(users, outfile, indent=4)
        
        print("Sign up successful. Go back and Log in")

    #User has to run the program again to login. Should figure out a way to refer back to login part of the code.
    #Should I just put everything under separate functions?
    if login_status == False:
        exit()
    
    #At this point I'm thinking should I divide this long code into functions.

    if os.path.exists(f'contacts/{user_id}.json'):
        print("File exists for user")
    else:
        with open(f'contacts/{user_id}.json', "w") as f:
            f.write("{\"data\": {}}")

    while True:
        user_choice = input("Choose operations you want:\n1. Show\n2. Add\n3. Remove\n4. Edit\n5.Exit App\n")
        if user_choice == "1":
            show_contact(user_id)
        if user_choice == "2":
            PN = input("Enter phone number: ")
            FN = input("Enter first name: ")
            LN = input("Enter last name: ")
            add_contact(user_id, PN, FN, LN)
        if user_choice == "3":
            PN_to_delete = input("Enter the Phone number of the person you want to delete: ")
            remove_contact(user_id, PN_to_delete)
        if user_choice == "4":
            edit_PN = input("Enter the phone number that you want to edit: ")
            edit_option = input("Choose edit option you want:\n1. FirstName\n2. LastName\n3. PhoneNumber")
            edit = input("Type the edit: ")
            edit_contact(user_id, edit_PN, edit_option, edit)
        if user_choice == "5":
            break

    

