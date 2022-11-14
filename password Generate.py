import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=:;'\}]{[/?.>,<"

password_length = input("Enter the desired password length, or leave it blank for a random length: ").strip()
password_length = random.randint(30, 300) if password_length == "" else int(password_length)
print("Your Generate Password is: " + "".join(random.choice(chars) for i in range(password_length)))
input("Enter to continue")