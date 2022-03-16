#!/usr/local/bin/python3
from pandas import concat
import Menu
import Security

# Python 3.9.7 64-bit

def main():

    # CURRENT USERNAME : sreshtaa
    # PASSWORD : pizza
    # Leaks: password containing "\n", source containing " : "

    object = Menu.Menu()
    object.print_menu()

    # object = Security.Security()
    # key = object.generate_key("pizza")

    # data = object.encrypt_file(key, "Vault.txt")
    # object.create_encrypted_file(data, "Vault.txt")
    
    # data = object.decrypt_file(key, "Vault.encrypted")
    # object.create_decrypted_file(data, "Vault.encrypted")

    # print(object.count_entries("Vault.encrypted"))

    # object.edit_source("Vault.encrypted", "ggmail", "gmail")

    # print(object.edit_password("Vault.encrypted", "instagram", "boring"))
    # object.print_data("Vault.encrypted")

    
    

if __name__ == "__main__":
    main()