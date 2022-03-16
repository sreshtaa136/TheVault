#!/usr/local/bin/python3
import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet, InvalidToken


class Security:

    def generate_key(self, password_input):
        password = password_input.encode() #Converting to type 'bytes'
        salt = b'Nwm\xb0\x9d=R\xaf-`\xeb\xc7\x94\xef\xf1\xbe\xdd\xa9\x93k\xda\xe6\xedk\x96\xa3\x1d\xfd\x85\x9f\x0c\xf1\xa2\xab\xed\xe4'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password)) 
        return key


    def encrypt_password(self, password):
        key = self.generate_key("Th1cc@$S")
        encoded_password = password.encode()
        fernet = Fernet(key)
        encrypted = fernet.encrypt(encoded_password)
        return encrypted


    def decrypt_password(self, encrypted_password):
        key = self.generate_key("Th1cc@$S")
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted_password)
        password = decrypted.decode()
        return password


    def encrypt_file(self, key, file_name):
        # Opening the file to encrypt
        with open(file_name, "rb") as f:
            data = f.read()

        fernet = Fernet(key)
        encrypted = fernet.encrypt(data)
        return encrypted
    

    def create_encrypted_file(self, encrypted_data, file_name):
        # Writing encrypted data
        name = file_name[0:(len(file_name)-4)]
        encrypted_file = name + ".encrypted"
        with open(encrypted_file, "wb") as f:
            f.write(encrypted_data)
        with open(file_name, "wb") as f:
            f.truncate(0)
        os.remove(file_name)


    def decrypt_file(self, key, file_name):
        # Decrypt the file
        with open(file_name, "rb") as f:
            data = f.read()
        fernet = Fernet(key)
        try:       
            decrypted = fernet.decrypt(data)
        except InvalidToken as e:
            print("Invalid Key - Unsuccessful decryption")
        return decrypted


    def create_decrypted_file(self, decrypted_data, file_name):
        # Writing decrypted data           
            n = len(file_name) - 10
            decrypted_file = file_name[0:n] + ".txt"
            with open(decrypted_file, "wb") as f:
                f.write(decrypted_data)
            with open(file_name, "wb") as f:
                f.truncate(0)
            os.remove(file_name)


    def lock_file(self, file_name):
        with open("key.key", "rb") as f:
            en_pwd = f.read()
        pwd = self.decrypt_password(en_pwd)
        key = self.generate_key(pwd)
        data = self.encrypt_file(key, file_name)
        self.create_encrypted_file(data, file_name)


    def unlock_file(self, file_name):
        with open("key.key", "rb") as f:
            en_pwd = f.read()
        pwd = self.decrypt_password(en_pwd)
        key = self.generate_key(pwd)
        data = self.decrypt_file(key, file_name)
        self.create_decrypted_file(data, file_name)
    

    def save_password(self, password):
        encrypted_password = self.encrypt_password(password)
        with open("key.key", "wb") as f:
            f.truncate(0)
            f.write(encrypted_password)


    def verify_password(self, password):
        with open("key.key", "rb") as f:
            encrypted_password = f.read()
        decrypted_password = self.decrypt_password(encrypted_password)
        if(password == decrypted_password):
            return True
        else:
            return False


    def make_entry(self, file_name, entry):

        self.unlock_file(file_name)
        with open("Vault.txt", "r") as f:
            contents = f.readlines()

        if("\n" in contents[len(contents)-1]):
            contents.append(entry + "\n")
        else:   
            contents.append("\n" + entry + "\n")   

        with open("Vault.txt", "w") as f:
            contents = "".join(contents)
            f.write(contents)  
        self.lock_file("Vault.txt")
    

    def count_entries(self, file_name):
        
        count = 0
        with open("key.key", "rb") as f:
            en_pwd = f.read()
        pwd = self.decrypt_password(en_pwd)
        key = self.generate_key(pwd)
        data_bytes = self.decrypt_file(key, file_name)
        data = data_bytes.decode('UTF-8')  
        data = data.splitlines()

        for entry in data:
            if (entry != ""):
                if (entry[0] == "*"):
                    count += 1
        return count
        
    
    def check_source(self, file_name, source):
        with open("key.key", "rb") as f:
            en_pwd = f.read()
        pwd = self.decrypt_password(en_pwd)
        key = self.generate_key(pwd)
        data_bytes = self.decrypt_file(key, file_name)
        data = data_bytes.decode('UTF-8')
        data = data.splitlines()

        for entry in data:
            if (entry != "" and entry[0] == "*"):
                divider_index = entry.find(" : ")
                src = entry[2:divider_index]
                if(src == source):
                    return data.index(entry)
        return -1


    def edit_source(self, file_name, source, new_source):

        # pwd_index = entry.find(" : ") + 3
        index = self.check_source(file_name, source)
        if(index == -1):
            return -1
        else:
            self.unlock_file(file_name)
            with open("Vault.txt", "r") as f:
                contents = f.readlines()
            
            divider_index = contents[index].find(" : ")
            before_src = contents[index][0:2]
            after_src = contents[index][divider_index:]
            new_src = new_source
            contents[index] = before_src + new_src + after_src

            with open("Vault.txt", "w") as f:
                contents = "".join(contents)
                f.write(contents) 
            self.lock_file("Vault.txt")

    
    def edit_password(self, file_name, source, new_password):
        index = self.check_source(file_name, source)
        if(index == -1):
            return -1
        else:
            self.unlock_file(file_name)
            with open("Vault.txt", "r") as f:
                contents = f.readlines()
            
            pwd_index = contents[index].find(" : ") + 3
            before_pwd = contents[index][0:pwd_index]
            new_pwd = new_password
            if(index != (len(contents)-1)):
                # old_pwd = contents[index][pwd_index: (len(contents[index])-2)]
                # before_pwd = contents[index][0:pwd_index]
                # after_pwd = contents[index][(pwd_index + len(new_password)):]
                after_pwd = "\n"
                contents[index] = before_pwd + new_pwd + after_pwd
            else:
                contents[index] = before_pwd + new_pwd

            with open("Vault.txt", "w") as f:
                contents = "".join(contents)
                f.write(contents) 
            self.lock_file("Vault.txt")

    
    def delete_entry(self, file_name, source):

        index = self.check_source(file_name, source)
        if(index == -1):
            return -1
        else:
            self.unlock_file(file_name)
            with open("Vault.txt", "r") as f:
                contents = f.readlines()
            
            del contents[index]

            with open("Vault.txt", "w") as f:
                contents = "".join(contents)
                f.write(contents) 
            self.lock_file("Vault.txt")


    def print_data(self, file_name):

        with open("key.key", "rb") as f:
            en_pwd = f.read()
        pwd = self.decrypt_password(en_pwd)
        key = self.generate_key(pwd)
        data_bytes = self.decrypt_file(key, file_name)
        data = data_bytes.decode('UTF-8') 
        print("\n---------------------------------------------------------------------") 
        print(data)
        print("\n---------------------------------------------------------------------")