import os
import getpass
import re
import pyAesCrypt

def validate_password(password):
    if len(password) < 10:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[!@#$%^&*()]", password):
        return False
    return True

def main():
    foldername = input("Enter the folder name: ")
    password = getpass.getpass("Enter the password: ")

    while not validate_password(password):
        print("Invalid password. It must be at least 10 characters long and include lowercase, uppercase, numbers, and special characters.")
        password = getpass.getpass("Enter the password: ")

    bufferSize = 64 * 1024
    
    
    # encrypt
    pyAesCrypt.encryptFile(str(foldername), str(foldername)+".aes", password, bufferSize)

if __name__ == '__main__':
    main()
