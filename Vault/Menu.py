#!/usr/local/bin/python3

import Security
import sys, time, os

class Menu:

    # TO DO:
    # MASK PASSWORD
    # IMPLEMENT EXIT
    object = Security.Security()

    def print_text(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.09)

    def create_account(self, username, password):
        with open("Vault.txt", "a") as f:
            f.truncate(0)
            details = "VAULT V1.0\n" + "Username: " + username + "\n\n"
            details += "Passwords: "
            f.write(details)
        
    def print_menu(self):
        print("\nWelcome to The Vault. You can type 'exit' any time you want to exit the application. \nAre you a ...")
        time.sleep(1)
        print("1. New User")
        time.sleep(1)
        print("2. Existing User\n")
        time.sleep(1)
        user_type = input("Please enter an option to proceed >> ")

        if(user_type == "1"):
            print("\nHello there! What would you like me to call you?")
            # time.sleep(1)
            username = input("Please enter a username >> ")
            # time.sleep(1)
            print("\nHello " + username + "! You will now create a secure password for your vault.")
            print("This password cannot be changed, and without it, you will lose all your data.")
            print("Hence, make sure you remember it.")
            # time.sleep(1)
            password = input("Please enter a secure password here >> ")
            password_double = input("Please re-enter your password to confirm >> ")
            # time.sleep(1)

            while (password != password_double):
                print("Oops! The passwords didn't match! Try again!")
                password = input("Please enter a secure password here >> ")
                password_double = input("Please re-enter your password to confirm >> ")

            print("\nYour account has been created successfully. You will now be able to make entries in your vault.")
            print("Each entry consists of:")
            print("1. The source (the application, website, card, or any type of source the password belongs to)")
            print("2. The key (your password for the source)")

    
        



