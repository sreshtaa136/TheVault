#!/usr/local/bin/python3
import Security
import Account
import sys, time

class Menu:

    # TO DO:
    # MASK PASSWORD
    
    def print_text(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.09)


    def exit_check(self, input):
        if(input == "logout"):
            try:
                with open("Vault.txt", "r") as f:
                    pass
            except FileNotFoundError:
                pass
            else:
                object = Security.Security()
                object.lock_file("Vault.txt")
            print("\n Exiting appliation...\n")
            exit(1)
    

    def print_menu(self):

        account_obj = Account.Account()
        security_obj = Security.Security()
        print("\nWelcome to The Vault. You can type 'logout' any time you want to exit the application. \nAre you a ...")
        print("1. New User")
        print("2. Existing User\n")
        user_type = input("Please enter an option to proceed >> ")
        self.exit_check(user_type)

        while(user_type != "1" and user_type != "2"):
            print("Invalid entry! Please enter a valid option!\n")
            print("1. New User")      
            print("2. Existing User\n")
            user_type = input("Enter a valid option to proceed >> ")
            self.exit_check(user_type)
                
        if(user_type == "1"):
            print("\nHello there! What would you like me to call you?")
            username = input("Please enter a username >> ")
            self.exit_check(username)              
            print("\nHello " + username + "! You will now create a secure password for your vault.")
            print("This password cannot be changed, and without it, you will lose all your data.")
            print("Hence, make sure you remember it.")
            password = input("Please enter a secure password here >> ")
            self.exit_check(password)   
            password_double = input("Please re-enter your password to confirm >> ")
            self.exit_check(password_double)   

            while (password != password_double):
                print("Oops! The passwords didn't match! Try again!")
                password = input("Please enter a secure password here >> ")
                self.exit_check(password) 
                password_double = input("Please re-enter your password to confirm >> ")
                self.exit_check(password_double)   

            account_obj.create_account(username, password)
            print("\nYour account has been created successfully. You will now be able to make entries in your vault.")
            print("Each entry consists of:")
            print("1. The source (the application, website, card, or any type of source the password belongs to)")
            print("2. The key (your password for the source)")

        elif(user_type == "2"):
            username = input("Please enter your username >> ")
            self.exit_check(username)  
            while (account_obj.verify_username(username) == False):
                print("Invalid username! Please enter a valid username!\n")
                username = input("Please enter your username >> ")
                self.exit_check(username)  
            
            password = input("Please enter your password >> ")
            self.exit_check(password)  
            count = 0

            while(security_obj.verify_password(password) == False):
                print("Invalid password! Number of attempts left: " + str(5 - count) + "\n")
                password = input("Please enter your password >> ")
                count += 1
                if(count == 5):
                    print("\n No more attempts left. Exiting appliation...\n")
                    exit(1)

            security_obj.unlock_file("Vault.encrypted")
            print("\nWelcome back " + username + "!")
            
        print("\n---------------------------------------------------------------------")
        print("Your current number of password entries: \n")
        print("1.Make a new entry")
        print("2.View passwords")
        print("3.Exit")
        print("\n---------------------------------------------------------------------")
        
        self.exit_check("logout") # COMMENT OUT LATER