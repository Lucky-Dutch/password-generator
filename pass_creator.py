"""
This program create random passwords.
"""
import random
import string
import datetime


print("Hello in Password Creator 0.01\n\
    Choose a right number: \n\
    1 - simple password with 6th letters\n\
    2 - password with letters (small and big) and numbers with your value of characters\n\
    3 - CRAZIEST passwords - try it yourself!\n\
    4 - I don't have idea of what I want to do")


program_choice = input("What number you choose?: ")

now = datetime.datetime.now()

now = now.strftime("%d-%m-%Y %X")

password = ""


if program_choice == "1":
    for i in range(6):
        password += random.choice(string.ascii_lowercase)

elif program_choice == "2":
    characters_value = input("Write how many characters your password need: ")
    for i in range(int(characters_value)):
        password += random.choice(string.ascii_letters + string.digits)
    if password.isalpha():
        password = password[:-1] + random.choice(string.digits)

elif program_choice == "3":
    characters_value = input("Write how many characters your password need: ")
    for i in range(int(characters_value)):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)

elif program_choice == "4":
    print("Thank you, see you next time")
    
else:
    print("Wrong key. Try it again.")
   
with open("passwords.txt","a+") as file:
    file.write("password: {}  website: {} datetime: {}\n".format(password,input("Write name of website or press enter: "), now))

print(password)
