import string
import random

characters_reg = (
    string.ascii_letters
)
characters_spc = (string.digits + string.punctuation + " ?/!@#$%^&*()_+")

password_length = int(input("How long do you want your password to be? "))

specical_characters = input("Do you want to use special characters? (y/n) ")

print(characters_reg)

if specical_characters == "y":
    characters = characters_reg + characters_spc
else:
    characters = characters_reg

print("Your password is: ")
for i in range(password_length):
    print(random.choice(characters), end="")
