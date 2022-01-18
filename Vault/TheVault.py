#!/usr/local/bin/python3
import Menu
import Security

def main():

    object = Menu.Menu()
    object.print_menu()

    # object = Security.Security()
    # key = object.generate_key("pizzass")
    # en_data = object.encrypt_file(key, "Vault.txt")
    # object.create_encrypted_file(en_data, "Vault.txt")
    # data = object.decrypt_file(key, "Vault.txt.encrypted")
    # object.create_decrypted_file(data, "Vault.txt.encrypted")
    # data = (object.decrypt_file(key, "Vault.txt.encrypted")).decode()
    # line = data[21:]
    # index = line.index("\n")
    # username = line[0:index]
    # object.exit_check("logout")
    
    
    
if __name__ == "__main__":
    main()