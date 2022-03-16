#!/usr/local/bin/python3
import Security
import Account
import sys, time
from os import system, name
from stdiomask import getpass

class Menu:
    
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


    def clear_screen(self):
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')


    def create_account(self):
        account_obj = Account.Account()
        print("\nHello there! What would you like me to call you?")
        username = input("Please enter a username >> ")
        self.exit_check(username)              
        print("\nHello " + username + "! You will now create a secure password for your vault.")
        print("This password cannot be changed, and without it, you will lose all your data.")
        print("Hence, make sure you remember it.")
        password = getpass(prompt = "Please enter a secure password here >> ", mask = "*")
        self.exit_check(password)   
        password_double = getpass(prompt = "Please re-enter your password to confirm >> ", mask = "*")
        self.exit_check(password_double)   

        while (password != password_double):
            print("Oops! The passwords didn't match! Try again!")
            password_double = getpass(prompt = "Please re-enter your password to confirm >> ", mask = "*")
            self.exit_check(password_double)   

        account_obj.create_account(username, password)
        print("\nYour account has been created successfully. You will now be able to make entries in your vault.")

    
    def user_login(self):
        account_obj = Account.Account()
        security_obj = Security.Security()
        username = input("Please enter your username >> ")
        self.exit_check(username)  
        while (account_obj.verify_username(username) == False):
            print("Invalid username! Please enter a valid username!\n")
            username = input("Please enter your username >> ")
            self.exit_check(username)  
        
        password = getpass(prompt = "Please enter your password >> ", mask = "*")
        self.exit_check(password)  
        count = 0

        while(security_obj.verify_password(password) == False):
            print("Invalid password! Number of attempts left: " + str(5 - count) + "\n")
            password = getpass(prompt = "Please enter your password >> ", mask = "*")
            self.exit_check(password)
            count += 1
            if(count == 5):
                print("\n No more attempts left. Exiting appliation...\n")
                exit(1)
        print("\nWelcome back " + username + "!")


    def make_entry(self):
        security_obj = Security.Security()
        print("\nEach entry consists of:")
        print("1. The source (the application, website, card, or any type of source the password belongs to)")
        print("2. The key (your password for the source)\nYou can type 'logout' any time you want to exit the application.")
        source = input("\nEnter a source >> ")
        self.exit_check(source)
        print("Your source is: " + source + ". Correct?")
        confirmation = input("Enter 'y' for Yes, 'n' for No >> ")
        self.exit_check(confirmation)

        while(confirmation.upper() != "Y" and confirmation.upper() != "N"):
            print("\nInvalid entry! Please enter a valid option!\n")
            confirmation = input("Enter 'y' for Yes, 'n' for No >> ")
            self.exit_check(confirmation)

        if (confirmation.upper() == "N"):
            while (confirmation.upper() == "N"):
                source = input("Enter a source >> ")
                self.exit_check(source)
                print("Your source is '" + source + "'. Correct?")
                confirmation = input("Enter 'y' for Yes, 'n' for No >> ")
                self.exit_check(confirmation)

                while(confirmation.upper() != "Y" and confirmation.upper() != "N"):
                    print("\nInvalid entry! Please enter a valid option!\n")
                    confirmation = input("Enter 'y' for Yes, 'n' for No >> ")
                    self.exit_check(confirmation)
        
        if (confirmation.upper() == "Y"):
            p = "\nEnter your password for '" + source + "' >> "
            password = getpass(prompt = p, mask = "*")
            self.exit_check(password)   
            password_double = getpass(prompt = "Please re-enter your password to confirm >> ", mask = "*")
            self.exit_check(password_double)   

            while (password != password_double):
                print("\nOops! The passwords didn't match! Try again!")
                password_double = getpass(prompt = "Please re-enter your password to confirm >> ", mask = "*")
                self.exit_check(password_double)  

        entry = "* " + source + " : " + password
        security_obj.make_entry("Vault.encrypted", entry)

    
    def print_passwords(self):
        security_obj = Security.Security()
        security_obj.print_data("Vault.encrypted")
        print("Note: The console will be cleared when you enter 'done'")
        x = input("Enter 'done' when ready >> ")
        self.exit_check(x)
        if(x == "done"):
            self.clear_screen()
        else:
            while(x != "done"):
                self.exit_check(x)
                print("Invalid input! Valid inputs are: done, logout")
                x = input("Enter 'done' when ready >> ")
            self.clear_screen()


    def edit_source(self):

        security_obj = Security.Security()
        src = input("Enter the name of the source you want to edit >> ")
        self.exit_check(src)
        check = security_obj.check_source("Vault.encrypted", src)

        while(check == -1):
            print("Invalid source! Please enter a valid source!\n")
            src = input("Enter the name of the source you want to edit >> ")
            self.exit_check(src)
            check = security_obj.check_source("Vault.encrypted", src)
        
        new_src = input("Enter the name of the new source to replace '" + src + "' >> ")
        self.exit_check(new_src)

        print("Your new source is '" + new_src + "', correct?")
        confirmation = input("Enter 'y' for Yes, 'n' for No >> ")
        self.exit_check(confirmation)

        while(confirmation.upper() != "Y" and confirmation.upper() != "N"):
            print("\nInvalid entry! Please enter a valid option!\n")
            confirmation = input("Enter 'y' for Yes, 'n' for No >> ")
            self.exit_check(confirmation)

        if (confirmation.upper() == "N"):
            while (confirmation.upper() == "N"):
                new_src = input("Enter the name of the new source to replace '" + src + "' >> ")
                self.exit_check(new_src)
                print("Your new source is '" + new_src + "', correct?")
                confirmation = input("Enter 'y' for Yes, 'n' for No >> ")
                self.exit_check(confirmation)

                while(confirmation.upper() != "Y" and confirmation.upper() != "N"):
                    print("\nInvalid entry! Please enter a valid option!\n")
                    confirmation = input("Enter 'y' for Yes, 'n' for No >> ")
                    self.exit_check(confirmation)             
        
        if (confirmation.upper() == "Y"):
            security_obj.edit_source("Vault.encrypted", src, new_src)
            print("Successfully changed the source '" + src + "' to '" + new_src + "'.")
            return new_src

    
    def edit_password(self, source):

        security_obj = Security.Security()
        password = getpass(prompt = "Enter a new password for '" + source + "' >> ", mask = "*")
        self.exit_check(password)   
        password_double = getpass(prompt = "Please re-enter your password to confirm >> ", mask = "*")
        self.exit_check(password_double)   

        while (password != password_double):
            print("Oops! The passwords didn't match! Try again!")
            password_double = getpass(prompt = "Please re-enter your password to confirm >> ", mask = "*")
            self.exit_check(password_double)  
        
        security_obj.edit_password("Vault.encrypted", source, password)
        print("Successfully changed the password entry for '" + source + "'.")


    def edit_entry(self):
        
        print("\nEach entry consists of:")
        print("1. The source (the application, website, card, or any type of source the password belongs to)")
        print("2. The key (your password for the source)\nYou can type 'logout' any time you want to exit the application.")
        print("Do you want to change the source or the password of the entry?")
        option = input("Enter 's' for source & 'p' for password >> ")
        self.exit_check(option)

        while(option != "s" and option != "p"):
            print("Invalid entry! Please enter a valid option!\n")
            print("Do you want to change the source or the password of the entry?")
            option = input("Enter 's' for source & 'p' for password >> ")
            self.exit_check(option)

        if(option == "s"):
            new_src = self.edit_source()
            print("Would you like to edit the password too?")
            confirmation = input("Enter 'y' for Yes, 'n' for No >> ")
            self.exit_check(confirmation)

            while(confirmation.upper() != "Y" and confirmation.upper() != "N"):
                print("\nInvalid entry! Please enter a valid option!\n")
                confirmation = input("Enter 'y' for Yes, 'n' for No >> ")
                self.exit_check(confirmation)

            if (confirmation.upper() == "N"):
                pass                      
            if (confirmation.upper() == "Y"):
                self.edit_password(new_src)
        
        elif(option == "p"):

            security_obj = Security.Security()
            src = input("Enter the name of the source whose password you want to edit >> ")
            self.exit_check(src)
            check = security_obj.check_source("Vault.encrypted", src)

            while(check == -1):
                print("Invalid source! Please enter a valid source!\n")
                src = input("Enter the name of the source you want to edit >> ")
                self.exit_check(src)
                check = security_obj.check_source("Vault.encrypted", src)

            self.edit_password(src)
        
    
    def delete_entry(self):

        security_obj = Security.Security()
        src = input("\nEnter the source of the entry you want to delete >> ")
        self.exit_check(src)
        check = security_obj.check_source("Vault.encrypted", src)

        while(check == -1):
            print("Invalid source! Please enter a valid source!\n")
            src = input("Enter the source of the entry you want to delete >> ")
            self.exit_check(src)
            check = security_obj.check_source("Vault.encrypted", src)

        print("You want to delete the entry for '" + src + "', correct?")
        confirmation = input("Enter 'y' for Yes, 'n' for No >> ")
        self.exit_check(confirmation)

        while(confirmation.upper() != "Y" and confirmation.upper() != "N"):
            print("\nInvalid entry! Please enter a valid option!\n")
            confirmation = input("Enter 'y' for Yes, 'n' for No >> ")
            self.exit_check(confirmation)

        if (confirmation.upper() == "N"):
            while (confirmation.upper() == "N"):
                src = input("Enter the source of the entry you want to delete >> ")
                self.exit_check(src)
                print("You want to delete the entry for '" + src + "', correct?")
                confirmation = input("Enter 'y' for Yes, 'n' for No >> ")
                self.exit_check(confirmation)

                while(confirmation.upper() != "Y" and confirmation.upper() != "N"):
                    print("\nInvalid entry! Please enter a valid option!\n")
                    confirmation = input("Enter 'y' for Yes, 'n' for No >> ")
                    self.exit_check(confirmation)             
        
        if (confirmation.upper() == "Y"):
            security_obj.delete_entry("Vault.encrypted", src)
            print("Successfully deleted the entry for '" + src + "'.")


    def print_menu(self):
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
            self.create_account()
        elif(user_type == "2"):
            self.user_login()
            
        while(True):
            
            count = str(security_obj.count_entries("Vault.encrypted"))
            print("\n---------------------------------------------------------------------")
            print("Your current number of password entries: " + count)
            print("1.Make a new entry")
            print("2.Edit an entry")
            print("3.Delete an entry")
            print("4.View passwords")
            print("5.Exit")
            print("\n---------------------------------------------------------------------")
            option = input("Please enter an option to proceed >> ")
            self.exit_check(option)
            
            while(option != "1" and option != "2" and option != "3"
                and option != "4" and option != "5"):

                print("Invalid entry! Please enter a valid option!\n")
                print("1.Make a new entry")
                print("2.Edit an entry")
                print("3.Delete an entry")
                print("4.View passwords")
                print("5.Exit")
                option = input("Enter a valid option to proceed >> ")
                self.exit_check(option)

            if (option == "1"):
                self.make_entry()
            elif(option == "2"):
                self.edit_entry()
            elif(option == "3"):
                self.delete_entry()
            elif(option == "4"):
                self.print_passwords()
            elif (option == "5"):
                self.exit_check("logout") 
