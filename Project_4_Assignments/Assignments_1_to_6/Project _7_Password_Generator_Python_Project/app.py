import random

def generate_password(length=8):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-=+[]{|}:,.<>?/"
    password = ""
    for _ in range(length):
        password += random.choice(characters)
    print("Generated password:", password)  

if __name__ == "__main__":
    generate_password()