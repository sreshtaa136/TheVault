#!/usr/local/bin/python3
import Security

class Account:

    def create_account(self, username, password):
        with open("Vault.txt", "a") as f:
            f.truncate(0)
            details = "VAULT V1.0\n" + "Username: " + username + "\n\n"
            details += "Passwords:"
            f.write(details)

        security_obj = Security.Security()
        security_obj.save_password(password)
    

    def verify_username(self, username):

        object = Security.Security()

        with open("key.key", "rb") as f:
            en_pwd = f.read()
        pwd = object.decrypt_password(en_pwd)

        key = object.generate_key(pwd)
        data = (object.decrypt_file(key, "Vault.encrypted")).decode()
        line = data[21:]
        index = line.index("\n")
        uname = line[0:index]
        if(uname == username):
            return True
        else:
            return False