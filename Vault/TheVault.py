#!/usr/local/bin/python3
import Menu
import Security


def main():

    # CURRENT USERNAME : sreshtaa
    # PASSWORD : pizza

    # with open("Vault.txt", "r") as f:
    #     contents = f.readlines()
    
    # for entry in contents:
    #     print(entry.rstrip())

    object = Menu.Menu()
    object.print_menu()

    # object = Security.Security()
    # key = object.generate_key("pizza")

    # data = object.encrypt_file(key, "Vault.txt")
    # object.create_encrypted_file(data, "Vault.txt")
    
    # data = object.decrypt_file(key, "Vault.encrypted")
    # object.create_decrypted_file(data, "Vault.encrypted")

    # print(object.count_entries("Vault.encrypted"))

    
    
if __name__ == "__main__":
    main()